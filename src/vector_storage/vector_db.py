from __future__ import annotations

import json
import os
import time
from abc import ABC, abstractmethod
from typing import Any

import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import cohere
import weave
from cohere import RerankResponse

from src.generation.summary_manager import SummaryManager
from src.utils.config import CHROMA_DB_DIR, COHERE_API_KEY, OPENAI_API_KEY, PROCESSED_DATA_DIR
from src.utils.decorators import base_error_handler
from src.utils.logger import configure_logging, get_logger

logger = get_logger()


class DocumentProcessor:
    def __init__(self):
        self.processed_dir = PROCESSED_DATA_DIR

    def load_json(self, filename: str) -> list[dict]:
        try:
            filepath = os.path.join(self.processed_dir, filename)
            with open(filepath) as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in file: {filename}")
            raise


class VectorDBInterface(ABC):
    @abstractmethod
    def prepare_documents(self, chunks: list[dict[str, Any]]) -> dict[str, list[str]]:
        pass

    @abstractmethod
    def add_documents(self, processed_docs: dict[str, list[str]]) -> None:
        pass

    @abstractmethod
    def query(self, user_query: str | list[str], n_results: int = 10) -> dict[str, Any]:
        pass

    @abstractmethod
    def reset_database(self) -> None:
        pass

    @abstractmethod
    def deduplicate_documents(self, search_results: dict[str, Any]) -> dict[str, Any]:
        pass

    @abstractmethod
    def check_documents_exist(self, document_ids: list[str]) -> tuple[bool, list[str]]:
        pass


class VectorDB(VectorDBInterface):
    def __init__(
        self,
        embedding_function: str = "text-embedding-3-small",
        openai_api_key: str = OPENAI_API_KEY,
    ):
        self.embedding_function = None
        self.client = None
        self.collection = None
        self.embedding_function_name = embedding_function
        self.openai_api_key = openai_api_key
        self.collection_name = "local-collection"
        self.summary_manager = SummaryManager()

        self._init()

    def _init(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DB_DIR)  # using default path for Chroma
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=self.openai_api_key, model_name=self.embedding_function_name
        )
        self.collection = self.client.get_or_create_collection(
            self.collection_name, embedding_function=self.embedding_function
        )
        logger.info(
            f"Successfully initialized ChromaDb with collection: {self.collection_name}\n with "
            f"{self.collection.count()} documents (chunks)"
        )

    def prepare_documents(self, chunks: list[dict]) -> dict[str, list[str]]:
        ids = []
        documents = []
        metadatas = []  # used for filtering

        for chunk in chunks:
            # extract headers
            data = chunk["data"]
            headers = data["headers"]
            header_text = " ".join(f"{key}: {value}" for key, value in headers.items() if value)

            # extract content
            content = data["text"]

            # combine
            combined_text = f"Headers: {header_text}\n\n Content: {content}"
            ids.append(chunk["chunk_id"])

            documents.append(combined_text)

            metadatas.append(
                {
                    "source_url": chunk["metadata"]["source_url"],
                    "page_title": chunk["metadata"]["page_title"],
                }
            )

        return {"ids": ids, "documents": documents, "metadatas": metadatas}

    @base_error_handler
    def add_documents(self, json_data: list[dict], file_name: str) -> None:
        processed_docs = self.prepare_documents(json_data)

        ids = processed_docs["ids"]
        documents = processed_docs["documents"]
        metadatas = processed_docs["metadatas"]

        # Check which documents are missing
        all_exist, missing_ids = self.check_documents_exist(ids)

        if all_exist:
            logger.info(f"All documents from {file_name} already loaded.")
        else:
            # Prepare data for missing documents only
            missing_indices = [ids.index(m_id) for m_id in missing_ids]
            missing_docs = [documents[i] for i in missing_indices]
            missing_metas = [metadatas[i] for i in missing_indices]

            # Add only missing documents
            self.collection.add(
                ids=missing_ids,
                documents=missing_docs,
                metadatas=missing_metas,
            )
            logger.info(f"Added {len(missing_ids)} new documents to ChromaDB.")

        # Generate summary for the entire file if not already present
        self.summary_manager.process_file(data=json_data, file_name=file_name)

    @base_error_handler
    def check_documents_exist(self, document_ids: list[str]) -> tuple[bool, list[str]]:
        """Checks if chunks are already added to the database based on chunk ids"""
        try:
            # Get existing document ids from the db
            result = self.collection.get(ids=document_ids, include=[])
            existing_ids = set(result["ids"])

            # Find missing ids
            missing_ids = list(set(document_ids) - existing_ids)
            all_exist = len(missing_ids) == 0

            if missing_ids:
                logger.info(f"{len(missing_ids)} out of {len(document_ids)} documents are new and will be added.")
            return all_exist, missing_ids

        except Exception as e:
            logger.error(f"Error checking document existence: {e}")
            return False, document_ids

    @base_error_handler
    def query(self, user_query: str | list[str], n_results: int = 10):
        """
        Handles both a single query and multiple queries
        """
        query_texts = [user_query] if isinstance(user_query, str) else user_query
        search_results = self.collection.query(
            query_texts=query_texts, n_results=n_results, include=["documents", "distances", "embeddings"]
        )
        return search_results

    @base_error_handler
    def reset_database(self):
        # Delete collection
        self.client.delete_collection(self.collection_name)

        self.collection = self.client.create_collection(
            self.collection_name, embedding_function=self.embedding_function
        )

        # Delete the summaries file
        self.summary_manager.clear_summaries()

        logger.info("Database reset successfully. ")

    def process_results_to_print(self, search_results: dict[str, Any]):
        documents = search_results["documents"][0]
        distances = search_results["distances"][0]

        output = []
        for docs, dist in zip(documents, distances, strict=True):
            output.append(f"Distance: {dist:.2f}\n\n{docs}")
        return output

    def deduplicate_documents(self, search_results: dict[str, Any]) -> dict[str, Any]:
        documents = search_results["documents"][0]
        distances = search_results["distances"][0]
        ids = search_results["ids"][0]

        unique_documents = {}

        for chunk_id, doc, distance in zip(ids, documents, distances, strict=True):
            if chunk_id not in unique_documents:
                unique_documents[chunk_id] = {"text": doc, "distance": distance}
        return unique_documents


class Reranker:
    def __init__(self, cohere_api_key: str = COHERE_API_KEY, model_name: str = "rerank-english-v3.0"):
        self.cohere_api_key = cohere_api_key
        self.model_name = model_name
        self.client = None

        self._init()

    def _init(self):
        try:
            self.client = cohere.ClientV2(api_key=self.cohere_api_key)
            logger.debug("Successfully initialized Cohere client")
        except Exception as e:
            logger.error(f"Error initializing Cohere client: {e}")
            raise

    def extract_documents_list(self, unique_documents: dict[str, Any]) -> list[str]:
        """
        Prepares the unique documents list for processing by Cohere.
        """
        # extract the 'text' field from each unique document
        document_texts = [chunk["text"] for chunk in unique_documents.values()]
        return document_texts

    def rerank(self, query: str, documents: dict[str, Any], return_documents=True) -> RerankResponse:
        """
        Use Cohere rerank API to score and rank documents based on the query.
        Excludes irrelevant documents.
        :return: list of documents with relevance scores
        """
        # extract list of documents
        document_texts = self.extract_documents_list(documents)

        # get indexed results
        response = self.client.rerank(
            model=self.model_name, query=query, documents=document_texts, return_documents=return_documents
        )

        logger.debug(f"Received {len(response.results)} documents from Cohere.")

        # filter irrelevant results
        # logger.debug(f"Filtering out the results with less than {relevance_threshold} relevance " f"score")
        # relevant_results = self.filter_irrelevant_results(response, relevance_threshold)
        # logger.debug(f"{len(relevant_results)} documents remaining after re-ranking.")

        return response


class ResultRetriever:
    def __init__(self, vector_db: VectorDB, reranker: Reranker):
        self.db = vector_db
        self.reranker = reranker

    @base_error_handler
    @weave.op()
    def retrieve(self, user_query: str, combined_queries: list[str], top_n: int = None):
        """Returns ranked documents based on the user query:
        top_n: The number of most relevant documents or indices to return, defaults to the length of the documents"""

        start_time = time.time()  # Start timing

        # get expanded search results
        search_results = self.db.query(combined_queries)
        unique_documents = self.db.deduplicate_documents(search_results)
        logger.info(f"Search returned {len(unique_documents)} unique chunks")

        # rerank the results
        ranked_documents = self.reranker.rerank(user_query, unique_documents)

        # filter irrelevnat results
        filtered_results = self.filter_irrelevant_results(ranked_documents, relevance_threshold=0.1)

        # limit the number of returned chunks
        limited_results = self.limit_results(filtered_results, top_n=top_n)

        # calculate time
        end_time = time.time()  # End timing
        search_time = end_time - start_time
        logger.info(f"Search and reranking completed in {search_time:.3f} seconds")

        return limited_results

    def filter_irrelevant_results(
        self, response: RerankResponse, relevance_threshold: float = 0.1
    ) -> dict[int, dict[str, int | float | str]]:
        """Filters out irrelevant result from Cohere reranking"""
        relevant_results = {}

        for result in response.results:
            relevance_score = result.relevance_score
            index = result.index
            text = result.document.text

            if relevance_score >= relevance_threshold:
                relevant_results[index] = {
                    "text": text,
                    "index": index,
                    "relevance_score": relevance_score,
                }

        return relevant_results

    def limit_results(self, ranked_documents: dict[str, Any], top_n: int = None) -> dict[str, Any]:
        """Takes re-ranked documents and returns n results"""

        if top_n is not None and top_n < len(ranked_documents):
            # Sort the items by relevance score in descending order
            sorted_items = sorted(ranked_documents.items(), key=lambda x: x[1]["relevance_score"], reverse=True)

            # Take the top N items and reconstruct the dictionary
            limited_results = dict(sorted_items[:top_n])

            logger.info(
                f"Returning {len(limited_results)} most relevant results (out of total {len(ranked_documents)} "
                f"results)."
            )
            return limited_results

        logger.info(f"Returning all {len(ranked_documents)} results")
        return ranked_documents


def main():
    configure_logging()
    vector_db = VectorDB()
    vector_db.reset_database()

    file = "langchain-ai_github_io_langgraph_20240928_143920-chunked.json"
    reader = DocumentProcessor()
    documents = reader.load_json(file)
    vector_db.add_documents(documents, file)


if __name__ == "__main__":
    main()
