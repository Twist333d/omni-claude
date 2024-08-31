import json
import os
import uuid
from typing import List, Dict, Any
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_DIR, BASE_DIR, ANTHROPIC_API_KEY
from llama_index.core import Document
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.node_parser import TokenTextSplitter
from anthropic import Anthropic, RateLimitError
import asyncio
from tqdm import tqdm
import time
import tiktoken
import markdown



# Set up logging
logger = setup_logger(__name__, 'chunking.log')

def error_handler(func):
    """Decorator to handle errors in both async and sync methods."""

    if asyncio.iscoroutinefunction(func):
        async def async_wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                return None
        return async_wrapper
    else:
        def sync_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                return None
        return sync_wrapper


class LlamaIndexLoader:
    """Loads JSON data using LlamaIndex."""
    def __init__(self, filename: str):
        """
        Initializes LlamaIndexLoader with the filename.

        Args:
            filename (str): The name of the JSON file to load.
        """
        self.filepath = os.path.join(RAW_DATA_DIR, filename)

    def load_json_data(self) -> List[Document]:
        """
        Loads JSON data from the file using LlamaIndex.

        Returns:
            List[Document]: A list of LlamaIndex Document objects.
        """
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)

            documents = []
            for page in data['data']:
                content = page.get('markdown', '')
                metadata = page.get('metadata', {})
                documents.append(Document(text=content, metadata=metadata))

            logger.info(f"Successfully loaded {len(documents)} documents from {self.filepath}")
            return documents

        except Exception as e:
            logger.error(f"Error loading data from {self.filepath}: {str(e)}")
            raise

class CustomMarkdownNodeParser(MarkdownNodeParser):
    """Custom Markdown parser to treat H1/H2 as top-level nodes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_nodes_from_documents(self, documents: List[Document]) -> List[Dict[str, Any]]:
        """
        Get nodes from documents.

        Args:
            documents (List[Document]): List of documents.

        Returns:
            List[Dict[str, Any]]: List of nodes.
        """
        nodes = []
        for document in documents:
            md_parser = markdown.Markdown(extensions=['fenced_code', 'tables'])
            parsed_text = md_parser.convert(document.text)

            current_chunk = None
            current_heading = None

            for line in parsed_text.split("\n"):
                if line.startswith("<h1>") or line.startswith("<h2>"):
                    if current_chunk is not None:
                        nodes.append(current_chunk)
                    current_heading = line.strip("<h1><h2>")
                    current_chunk = {
                        "text": "",
                        "metadata": {
                            "heading": current_heading,
                            "sourceURL": document.metadata.get('sourceURL', 'Unknown URL')
                        }
                    }
                elif line.strip() == "<hr>":  # Treat horizontal rules as separators
                    if current_chunk is not None:
                        nodes.append(current_chunk)
                    current_chunk = None
                    current_heading = None
                elif current_chunk is not None:
                    current_chunk["text"] += line + "\n"

            if current_chunk is not None:
                nodes.append(current_chunk)

        return nodes


class LlamaIndexChunker:
    """Chunks Markdown content using LlamaIndex."""

    def __init__(self, min_tokens: int = 800, max_tokens: int = 1200):
        """
        Initializes LlamaIndexChunker.

        Args:
            min_tokens (int): Minimum tokens per chunk.
            max_tokens (int): Maximum tokens per chunk.
        """
        self.min_tokens = min_tokens
        self.max_tokens = max_tokens
        self.text_splitter = TokenTextSplitter(chunk_size=max_tokens, chunk_overlap=100)
        self.node_parser = CustomMarkdownNodeParser(text_splitter=self.text_splitter, include_metadata=True)
        self.token_counter = TokenCounter()

    def chunk_markdown(self, content: str, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Chunks the Markdown content using LlamaIndex.

        Args:
            content (str): The Markdown content to chunk.
            metadata (Dict[str, Any]): Metadata associated with the content.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each representing a chunk.
        """
        document = Document(text=content, metadata=metadata)
        nodes = self.node_parser.get_nodes_from_documents([document])

        chunks = []
        for node in nodes:
            chunk_content = node.text
            chunk_metadata = node.metadata
            current_token_count = self.token_counter.count_tokens(chunk_content)

            # Split if chunk exceeds max tokens
            if current_token_count > self.max_tokens:
                split_chunks = self._split_chunk(chunk_content, chunk_metadata)
                chunks.extend(split_chunks)
            else:
                chunk = {
                    "chunk_id": str(uuid.uuid4()),
                    "source_url": chunk_metadata.get('sourceURL', 'Unknown URL'),
                    "main_heading": chunk_metadata.get('heading', 'No Heading'),
                    "content": chunk_content,
                    "summary": ""
                }
                chunks.append(chunk)

        return chunks

    def _split_chunk(self, content: str, metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Splits a chunk that exceeds the maximum token limit at paragraph breaks."""
        split_chunks = []
        remaining_content = content
        current_heading = metadata.get('heading', 'No Heading')

        while self.token_counter.count_tokens(remaining_content) > self.max_tokens:
            split_index = self._find_last_paragraph_break(remaining_content)

            if split_index != -1:
                chunk_content = remaining_content[:split_index].strip()
                chunk = {
                    "chunk_id": str(uuid.uuid4()),
                    "source_url": metadata.get('sourceURL', 'Unknown URL'),
                    "main_heading": current_heading,
                    "content": chunk_content,
                    "summary": ""
                }
                split_chunks.append(chunk)

                remaining_content = remaining_content[split_index:].strip()
                # No need to update heading as we're splitting at paragraph breaks
            else:
                # If no suitable split point is found, create a single large chunk
                chunk = {
                    "chunk_id": str(uuid.uuid4()),
                    "source_url": metadata.get('sourceURL', 'Unknown URL'),
                    "main_heading": current_heading,
                    "content": remaining_content,
                    "summary": ""
                }
                split_chunks.append(chunk)
                break

        # Add the last remaining chunk
        if remaining_content:
            chunk = {
                "chunk_id": str(uuid.uuid4()),
                "source_url": metadata.get('sourceURL', 'Unknown URL'),
                "main_heading": current_heading,
                "content": remaining_content,
                "summary": ""
            }
            split_chunks.append(chunk)

        return split_chunks

    def _find_last_paragraph_break(self, content: str) -> int:
        """Finds the index of the last paragraph break within token limits."""
        paragraph_break = content.rfind("\n\n")
        if paragraph_break != -1 and self.token_counter.count_tokens(
                content[:paragraph_break]) <= self.max_tokens:
            return paragraph_break
        return -1

class TokenCounter:
    """Counts tokens in text using tiktoken."""
    def __init__(self, model_name="cl100k_base"):
        """
        Initializes TokenCounter with the specified encoding model.

        Args:
            model_name (str): The name of the tiktoken encoding model. Defaults to "cl100k_base".
        """
        self.encoder = tiktoken.get_encoding(model_name)

    def count_tokens(self, text: str) -> int:
        """
        Counts the number of tokens in the given text.

        Args:
            text (str): The text to count tokens in.

        Returns:
            int: The number of tokens in the text.
        """
        return len(self.encoder.encode(text))

class Validator:
    """Validates the structure and completeness of processed chunks."""

    def validate_chunk_structure(self, chunk: Dict[str, Any]) -> bool:
        """
        Checks if a chunk has the required keys.

        Args:
            chunk (Dict[str, Any]): The chunk to validate.

        Returns:
            bool: True if the chunk has all required keys, False otherwise.
        """
        required_keys = ['chunk_id', 'source_url', 'main_heading', 'content']
        missing_keys = [key for key in required_keys if key not in chunk]
        if missing_keys:
            logger.error(f"Invalid chunk structure. Missing keys: {missing_keys} in chunk {chunk['chunk_id']}")
            return False
        return True

    def validate_completeness(self, original_content: str, processed_chunks: List[Dict[str, Any]]) -> bool:
        """
        Validates the completeness of the chunking process.

        Args:
            original_content (str): The original Markdown content.
            processed_chunks (List[Dict[str, Any]]): The list of processed chunks.

        Returns:
            bool: True if the chunking process is deemed complete, False otherwise.
        """
        original_content_length = len(original_content)
        processed_content_length = sum(len(chunk['content']) for chunk in processed_chunks)

        if abs(original_content_length - processed_content_length) / original_content_length > 0.05:
            logger.warning(
                f"Significant content length mismatch. Original: {original_content_length}, Processed: {processed_content_length}, Difference: {abs(original_content_length - processed_content_length)}")
            return False

        return True



class SummaryGenerator:
    """Generates summaries for chunks of text using the Anthropic API."""

    def __init__(self, api_key=ANTHROPIC_API_KEY, max_concurrent_requests=300):
        """
        Initializes SummaryGenerator with API key and concurrency settings.

        Args:
            api_key (str): The Anthropic API key. Defaults to ANTHROPIC_API_KEY from config.
            max_concurrent_requests (int): The maximum number of concurrent requests to the API. Defaults to 5.
        """
        self.client = Anthropic(api_key=api_key)
        self.max_concurrent_requests = max_concurrent_requests
        self.system_prompt = """You are an AI assistant specializing in summarizing technical documentation. Your task is to create concise, accurate summaries of various sections of a software documentation. These summaries will be used in a search pipeline to help users quickly find relevant information."""

    async def generate_summaries(self, chunks: List[Dict[str, Any]], pbar: tqdm) -> List[Dict[str, Any]]:
        """
        Generates summaries for a list of chunks.

        Args:
            chunks (List[Dict[str, Any]]): The list of chunks to generate summaries for.
            pbar (tqdm): A tqdm progress bar instance.

        Returns:
            List[Dict[str, Any]]: The list of chunks with summaries added.
        """
        semaphore = asyncio.Semaphore(self.max_concurrent_requests)
        tasks = [self._process_chunk(chunk, chunks, semaphore, pbar) for chunk in chunks]  # Pass 'chunks' here
        summarized_chunks = await asyncio.gather(*tasks)
        return summarized_chunks

    async def _process_chunk(self, chunk: Dict[str, Any], all_chunks: List[Dict[str, Any]], semaphore: asyncio.Semaphore, pbar: tqdm) -> Dict[str, Any]:
        """
        Processes a single chunk, generating its summary.

        Args:
            chunk (Dict[str, Any]): The chunk to process.
            semaphore (asyncio.Semaphore): A semaphore to control concurrency.
            pbar (tqdm): A tqdm progress bar instance.

        Returns:
            Dict[str, Any]: The chunk with the generated summary.
        """
        async with semaphore:
            try:
                context = self._gather_context(chunk, all_chunks)  # Pass all_chunks here
                messages = [
                    {"role": "user", "content": self._create_prompt(chunk, context)}
                ]

                response = await asyncio.to_thread(
                    self.client.messages.create,
                    model="claude-3-haiku-20240307",
                    max_tokens=300,
                    messages=messages,
                    system=self.system_prompt
                )

                chunk['summary'] = response.content[0].text
            except RateLimitError:
                await asyncio.sleep(1)  # Wait for 1 second before retrying
                return await self._process_chunk(chunk, semaphore, pbar)
            except Exception as e:
                logger.error(f"Error processing chunk {chunk['chunk_id']}: {str(e)}")
                chunk['summary'] = ""
            finally:
                pbar.update(1)
        return chunk

    def _gather_context(self, chunk: Dict[str, Any], all_chunks: List[Dict[str, Any]], context_window: int = 1) -> str:
        """
        Gathers context for the chunk from surrounding chunks.

        Args:
            chunk (Dict[str, Any]): The chunk to gather context for.
            all_chunks (List[Dict[str, Any]]): The list of all processed chunks.
            context_window (int): The number of chunks to consider before and after the current chunk. Defaults to 2.

        Returns:
            str: The gathered context as a string.
        """
        chunk_index = all_chunks.index(chunk)
        context = []

        # Gather context from previous chunks
        for i in range(max(0, chunk_index - context_window), chunk_index):
            prev_chunk = all_chunks[i]
            context.append(f"Previous H1: {prev_chunk['main_heading']}")
            context.append(f"Previous Excerpt: {self._get_brief_excerpt(prev_chunk['content'])}")

        # Gather context from next chunks
        for i in range(chunk_index + 1, min(chunk_index + context_window + 1, len(all_chunks))):
            next_chunk = all_chunks[i]
            context.append(f"Next H1: {next_chunk['main_heading']}")
            context.append(f"Next Excerpt: {self._get_brief_excerpt(next_chunk['content'])}")

        return "\n".join(context)

    def _get_brief_excerpt(self, content: str, max_length: int = 150) -> str:
        """
        Extracts a brief excerpt from the content.

        Args:
            content (str): The content to extract the excerpt from.
            max_length (int): The maximum length of the excerpt. Defaults to 100.

        Returns:
            str: A brief excerpt from the content.
        """
        excerpt = content.strip().replace('\n', ' ')
        return excerpt[:max_length] + "..." if len(excerpt) > max_length else excerpt

    def _create_prompt(self, chunk: Dict[str, Any], context: str) -> str:
        """
        Creates a prompt for the Anthropic API to generate a summary.

        Args:
            chunk (Dict[str, Any]): The chunk to summarize.
            context (str): The context for the chunk.

        Returns:
            str: The generated prompt.
        """
        return f"""
        Context: {context}

        Content to summarize:
        Heading: {chunk['main_heading']}
        {chunk['content']}

        Provide a brief, information-dense summary of the above content in 2-3 sentences. Capture the key technical points, focusing on the main ideas and their significance. This summary will be used in a search pipeline to answer user queries, so ensure it's highly relevant and precise.

        Your response should:
        1. Start immediately with the summary, without any preamble.
        2. Be accurate and use appropriate technical terminology.
        3. Be concise yet comprehensive, covering the most important aspects.

        Summary:
        """


class MainProcessor:
    """Orchestrates the entire chunking and summarizing process."""

    def __init__(self, filename: str, max_pages: int = 3):
        """
        Initializes MainProcessor with filename and dependencies.

        Args:
            filename (str): The name of the JSON file containing the data.
            max_pages (int): Maximum number of pages to process. Defaults to 3.
        """
        self.filename = filename
        self.max_pages = max_pages
        self.data_loader = LlamaIndexLoader(filename)
        self.chunker = LlamaIndexChunker()
        # self.summary_generator = SummaryGenerator()
        self.token_counter = TokenCounter()

    @error_handler
    async def process_data(self) -> List[Dict[str, Any]]:
        """Processes the data, from loading to summarizing and saving."""
        start_time = time.time()
        documents = self.data_loader.load_json_data()

        all_processed_chunks = []
        total_h1_count = 0
        total_h2_count = 0

        documents_to_process = documents[:self.max_pages]

        total_chunks = sum(
            len(self.chunker.chunk_markdown(doc.text, doc.metadata))
            for doc in documents_to_process
        )

        logger.info(f"Total chunks to process: {total_chunks}")

        with tqdm(total=total_chunks, desc="Processing chunks") as pbar:
            for doc in documents_to_process:
                content = doc.text  # Access text directly
                metadata = doc.metadata  # Access metadata directly
                source_url = metadata.get('sourceURL', 'Unknown URL')

                logger.info(f"Processing page: {source_url}")

                chunks = self.chunker.chunk_markdown(content, metadata)
                all_processed_chunks.extend(chunks)

                # Count headings (this may need adjustment based on how LlamaIndex handles headings)
                h1_count = content.count('\n# ')
                h2_count = content.count('\n## ')
                total_h1_count += h1_count
                total_h2_count += h2_count

                # Validate output
                if not Validator.validate_completeness(content, chunks, {'h1': h1_count, 'h2': h2_count}):
                    logger.error(f"Validation failed for page: {source_url}")
                    logger.error(f"Processed chunks sample: {chunks[:3]}")

                for chunk in chunks:
                    if not Validator.validate_chunk_structure(chunk):
                        logger.error(f"Invalid chunk structure for chunk: {chunk['chunk_id']}")

        self._save_chunks(all_processed_chunks)
        self._log_summary_statistics(all_processed_chunks, total_h1_count, total_h2_count)

        return all_processed_chunks

    def _save_chunks(self, all_processed_chunks: List[Dict[str, Any]]):
        """Saves the processed chunks to a JSON file."""
        input_base_name = os.path.splitext(self.filename)[0]

        # Create a new filename for the output
        output_filename = f"chunked_{input_base_name}.json"

        output_file = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "processed", output_filename)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, 'w') as f:
            json.dump(all_processed_chunks, f, indent=2)
        logger.info(f"Saved processed and summarized chunks to {output_file}")

    def _log_summary_statistics(self, all_processed_chunks: List[Dict[str, Any]], total_h1_count: int, total_h2_count: int):
        """Logs summary statistics about the processed chunks."""
        chunk_sizes = [len(chunk['content']) for chunk in all_processed_chunks]
        token_counts = [self.token_counter.count_tokens(chunk['content']) for chunk in all_processed_chunks]

        logger.info(f"\nSummary Statistics:")
        logger.info(f"Total number of chunks: {len(all_processed_chunks)}")
        logger.info(f"Total h1 headings: {total_h1_count}")
        logger.info(f"Total h2 headings: {total_h2_count}")
        logger.info(f"Average chunk size (characters): {sum(chunk_sizes) / len(chunk_sizes):.2f}")
        logger.info(f"Min chunk size (characters): {min(chunk_sizes)}")
        logger.info(f"Max chunk size (characters): {max(chunk_sizes)}")
        logger.info(f"Average token count per chunk: {sum(token_counts) / len(token_counts):.2f}")
        logger.info(f"Min token count: {min(token_counts)}")
        logger.info(f"Max token count: {max(token_counts)}")

        size_ranges = [(0, 500), (501, 1000), (1001, 1500), (1501, 2000), (2001, float('inf'))]
        size_distribution = {f"{start}-{end}": sum(start <= size < end for size in chunk_sizes) for start, end in size_ranges}
        logger.info("Chunk size distribution:")
        for range_str, count in size_distribution.items():
            logger.info(f"  {range_str} characters: {count} chunks")

async def main():
    filename = "supabase.com_docs__20240830_073045.json"
    max_pages = 5  # Set the number of pages you want to process here
    processor = MainProcessor(filename, max_pages=max_pages)
    await processor.process_data()

if __name__ == "__main__":
    asyncio.run(main())