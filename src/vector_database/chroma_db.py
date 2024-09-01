import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from typing import List, Dict, Any
import json
import os


from src.utils.config import OPENAI_API_KEY, PERSIST_DIRECTORY, LOG_DIR
from src.utils.logger import setup_logger

# Set up logger
logger = setup_logger("vector_db", os.path.join(LOG_DIR, "vector_db.log"))


class VectorDB:
    def __init__(self, persist_directory: str = PERSIST_DIRECTORY, collection_name: str = "supabase_docs"):
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(path=persist_directory)

        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=OPENAI_API_KEY,
            model_name="text-embedding-3-small"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )
        logger.info(f"Initialized VectorDB with collection '{collection_name}' in {persist_directory}")

    def add(self, chunks: List[Dict[str, Any]], batch_size: int = 2000):
        """
        Add documents to the collection.
        """
        total_chunks = len(chunks)
        for i in range(0, total_chunks, batch_size):
            batch = chunks[i:i + batch_size]

            documents = [
                f"Headers: {json.dumps(chunk['headers'])}\n\nContent: {chunk['content']}"
                for chunk in batch
            ]

            metadatas = [
                {
                    "source_url": chunk["source_url"],
                    "headers": json.dumps(chunk["headers"]),
                    "token_count": chunk["token_count"],
                    "has_code_block": chunk["has_code_block"]
                }
                for chunk in batch
            ]

            ids = [chunk["chunk_id"] for chunk in batch]

            self.collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            logger.info(f"Added batch of {len(batch)} chunks. Progress: {i+len(batch)}/{total_chunks}")

    def query(self, query_texts: List[str], n_results: int = 3, where: Dict[str, Any] = None):
        """
        Query the collection.
        """
        results = self.collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=where
        )
        logger.info(f"Executed query with {len(query_texts)} texts, requesting {n_results} results each.")
        return results

    def update(self, chunk_id: str, new_content: str, new_metadata: Dict[str, Any]):
        """
        Update a specific document in the collection.
        """
        self.collection.update(
            ids=[chunk_id],
            documents=[f"Headers: {json.dumps(new_metadata['headers'])}\n\nContent: {new_content}"],
            metadatas=[new_metadata]
        )
        logger.info(f"Updated document with id: {chunk_id}")

    def delete(self, chunk_ids: List[str]):
        """
        Delete specific documents from the collection.
        """
        self.collection.delete(ids=chunk_ids)
        logger.info(f"Deleted {len(chunk_ids)} documents from the collection.")

    def get(self, chunk_id: str):
        """
        Retrieve a specific document by its ID.
        """
        result = self.collection.get(ids=[chunk_id])
        logger.info(f"Retrieved document with id: {chunk_id}")
        return result

    def count(self):
        """
        Get the total number of documents in the collection.
        """
        count = self.collection.count()
        logger.info(f"Total documents in collection: {count}")
        return count

    def peek(self, limit: int = 10):
        """
        List a sample of documents in the collection.
        """
        sample = self.collection.peek(limit=limit)
        logger.info(f"Peeked at {limit} documents in the collection.")
        return sample

    def create_index(self):
        """
        Create or recreate the index for faster queries.
        """
        self.collection.create_index()
        logger.info("Created index for the collection.")

    def reset(self):
        """
        Reset the entire collection, removing all data.
        """
        self.client.delete_collection(self.collection_name)
        self.collection = self.client.create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_function
        )
        logger.info(f"Reset collection '{self.collection_name}'.")