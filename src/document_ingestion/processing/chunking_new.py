import json
import uuid
from typing import List, Dict, Any
from markdown import Markdown
import tiktoken
import asyncio
from tqdm import tqdm
import logging
import os
from langchain_text_splitters import MarkdownHeaderTextSplitter


from src.utils.config import BASE_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, LOG_DIR, GOOGLE_API_KEY
from src.utils.logger import setup_logger

logger = setup_logger(__name__, 'chunking.log', level=logging.DEBUG)



class InputProcessor:
    """Handles loading and validating the input JSON data."""

    def __init__(self, file_name: str):
        """Initialize the InputProcessor with the input file name."""
        self.file_path = os.path.join(RAW_DATA_DIR, file_name)

    def load_json(self) -> Dict[str, Any]:
        """Load JSON data from the file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in input file: {e}")
        except IOError as e:
            raise IOError(f"Error reading input file: {e}")

    def validate_input(self, data: Dict[str, Any]) -> bool:
        """Validate the structure of the input data."""
        if not isinstance(data, dict):
            return False
        if 'base_url' not in data or not isinstance(data['base_url'], str):
            return False
        if 'timestamp' not in data or not isinstance(data['timestamp'], str):
            return False
        if 'data' not in data or not isinstance(data['data'], list):
            return False
        for page in data['data']:
            if not isinstance(page, dict):
                return False
            if 'markdown' not in page or not isinstance(page['markdown'], str):
                return False
            if 'metadata' not in page or not isinstance(page['metadata'], dict):
                return False
        return True


class CustomMarkdownParser:
    def __init__(self, max_tokens: int = 1000):
        self.max_tokens = max_tokens
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def parse_markdown(self, content: str, source_url: str) -> List[Dict[str, Any]]:
        lines = content.split('\n')
        chunks = []
        current_chunk = {"content": "", "headers": {"H1": "", "H2": ""}, "source_url": source_url}

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Check for H1
            if i < len(lines) - 1 and set(lines[i + 1]) == {'='}:
                if current_chunk["content"]:
                    chunks.append(self._finalize_chunk(current_chunk))
                current_chunk = {"content": line + '\n' + lines[i + 1] + '\n', "headers": {"H1": line, "H2": ""},
                                 "source_url": source_url}
                i += 2
                continue

            # Check for H2
            if i < len(lines) - 1 and set(lines[i + 1]) == {'-'}:
                if current_chunk["content"]:
                    chunks.append(self._finalize_chunk(current_chunk))
                current_chunk = {"content": line + '\n' + lines[i + 1] + '\n',
                                 "headers": {"H1": current_chunk["headers"]["H1"], "H2": line},
                                 "source_url": source_url}
                i += 2
                continue

            # Check for H3
            if line.startswith('### '):
                if current_chunk["content"]:
                    chunks.append(self._finalize_chunk(current_chunk))
                current_chunk = {"content": line + '\n', "headers": current_chunk["headers"], "source_url": source_url}
                i += 1
                continue

            # Handle code blocks
            if line.startswith('```'):
                code_block = [line]
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_block.append(lines[i])
                    i += 1
                if i < len(lines):
                    code_block.append(lines[i])
                current_chunk["content"] += '\n'.join(code_block) + '\n'
                i += 1
                continue

            # Add line to current chunk
            current_chunk["content"] += line + '\n'
            i += 1

        if current_chunk["content"]:
            chunks.append(self._finalize_chunk(current_chunk))

        return chunks

    def _finalize_chunk(self, chunk: Dict[str, Any]) -> Dict[str, Any]:
        chunk["chunk_id"] = str(uuid.uuid4())
        chunk["token_count"] = len(self.tokenizer.encode(chunk["content"]))
        chunk["has_code_block"] = '```' in chunk["content"]
        return chunk

    def _split_oversized_chunk(self, chunk: Dict[str, Any]) -> List[Dict[str, Any]]:
        lines = chunk["content"].split('\n')
        sub_chunks = []
        current_sub_chunk = chunk.copy()
        current_sub_chunk["content"] = ""
        current_sub_chunk["token_count"] = 0

        for line in lines:
            line_tokens = len(self.tokenizer.encode(line))
            if current_sub_chunk["token_count"] + line_tokens > self.max_tokens:
                if current_sub_chunk["content"]:
                    sub_chunks.append(current_sub_chunk)
                    current_sub_chunk = chunk.copy()
                    current_sub_chunk["content"] = ""
                    current_sub_chunk["token_count"] = 0

            current_sub_chunk["content"] += line + '\n'
            current_sub_chunk["token_count"] += line_tokens

        if current_sub_chunk["content"]:
            sub_chunks.append(current_sub_chunk)

        for i, sub_chunk in enumerate(sub_chunks):
            sub_chunk["chunk_id"] = f"{chunk['chunk_id']}_part{i + 1}"

        return sub_chunks

class Chunker:
    def __init__(self, max_tokens: int = 1000):
        self.parser = CustomMarkdownParser(max_tokens)

    def parse_markdown(self, markdown_content: str, source_url: str) -> List[Dict[str, Any]]:
        chunks = self.parser.parse_markdown(markdown_content, source_url)
        final_chunks = []

        for chunk in chunks:
            if chunk["token_count"] > self.parser.max_tokens:
                sub_chunks = self.parser._split_oversized_chunk(chunk)
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(chunk)

        return final_chunks

class Summarizer:
    """Handles generating summaries for chunks using Google Gemini 1.5 Flash."""

    def __init__(self, api_key: str):
        """Initialize the Summarizer with the API key for Google Gemini 1.5 Flash."""
        self.api_key = api_key

    async def batch_summarize(self, chunks: List[Dict[str, Any]]) -> List[str]:
        """Generate summaries for a batch of chunks."""
        pass

    async def retry_api_call(self, func, max_retries: int = 3, backoff_factor: float = 1.5):
        """Retry an API call with exponential backoff."""
        pass

class Validator:
    """Handles validation of chunks and generates a validation report."""

    def validate_headings_preserved(self, original_doc: str, chunks: List[Dict[str, Any]]) -> bool:
        """Check if all H1 and H2 headings from the original document are preserved in the chunks."""
        pass

    def validate_token_counts(self, original_doc: str, chunks: List[Dict[str, Any]]) -> bool:
        """Validate that the total token count of chunks matches the original document (within a threshold)."""
        pass

    def generate_validation_report(self, original_doc: str, chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate a comprehensive validation report."""
        pass

class StatisticsGenerator:
    """Generates statistics about the chunking process."""

    def generate_statistics(self, original_docs: List[str], chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate comprehensive statistics about the chunking process."""
        pass

class Orchestrator:
    """Coordinates the entire chunking and processing workflow."""

    def __init__(self, input_file: str, output_file: str, api_key: str):
        """Initialize the Orchestrator with input/output files and API key."""
        self.input_file = input_file
        self.output_file = output_file
        self.input_processor = InputProcessor(input_file)
        self.chunker_and_enricher = Chunker()
        self.summarizer = Summarizer(api_key)
        self.validator = Validator()
        self.statistics_generator = StatisticsGenerator()

    async def run(self):
        """Run the entire chunking and processing workflow."""
        pass

    async def process_document(self, doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Process a single document through the chunking pipeline."""
        pass

    async def summarize_chunks(self, chunks: List[Dict[str, Any]]) -> List[str]:
        """Generate summaries for a list of chunks."""
        pass

    def validate_and_report(self, original_doc: str, chunks: List[Dict[str, Any]]):
        """Validate the chunks and generate a report."""
        pass

if __name__ == "__main__":
    input_file = "path/to/input.json"
    output_file = "path/to/output.json"
    api_key = "your_google_gemini_api_key"

    orchestrator = Orchestrator(input_file, output_file, api_key)
    asyncio.run(orchestrator.run())