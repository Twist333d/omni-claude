import json
import os
from typing import List, Dict, Any
import markdown
import tiktoken
from anthropic import Anthropic

# Import our custom logger and config
from src.utils.logger import setup_logger
from src.utils.config import API_KEY, RAW_DATA_DIR

# Set up logging
logger = setup_logger(__name__, "chunking.log")

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
INPUT_FILE = os.path.join(RAW_DATA_DIR, "supabase.com_docs__20240826_201304.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "processed", "chunked_supabase_docs.json")
TARGET_CHUNK_SIZE = 1000
CHUNK_SIZE_TOLERANCE = 0.2

# Initialize Anthropic client
anthropic = Anthropic(api_key=API_KEY)

class DataProcessor:
    def load_data(self, file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            logger.info(f"Successfully loaded data from {file_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {str(e)}")
            raise

    def extract_page_content(self, page: Dict[str, Any]) -> str:
        return page.get('markdown', '')

    def remove_boilerplate(self, content: str) -> str:
        # TODO: Implement boilerplate removal if necessary
        return content

class ChunkCreator:
    """ # TODO: Implement ChunkCreator"""

class SummaryGenerator:
    """# TODO: Implement SummaryGenerator"""

class OutputFormatter:
    """# TODO: Implement OutputFormatter"""

class MainProcessor:
    """# TODO: Implement MainProcessor"""


def main():
    processor = DataProcessor()
    raw_data = processor.load_data(INPUT_FILE)

    # Test with the first page
    if raw_data['data']:
        first_page = raw_data['data'][0]
        content = processor.extract_page_content(first_page)
        cleaned_content = processor.remove_boilerplate(content)

        logger.info(f"Processed content length: {len(cleaned_content)}")
        logger.info(f"First 500 characters:\n{cleaned_content[:500]}")
    else:
        logger.warning("No data found in the input file.")

if __name__ == "__main__":
    main()