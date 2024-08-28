import json
import os
import uuid
from typing import List, Dict, Any
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_DIR, BASE_DIR
import anthropic
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
import tiktoken

# Set up logging
logger = setup_logger(__name__, "chunking.py")


class DataLoader:
    def __init__(self, filename: str):
        self.filepath = os.path.join(RAW_DATA_DIR, filename)

    def load_json_data(self) -> Dict[str, Any]:
        try:
            with open(self.filepath, 'r') as f:
                data = json.load(f)
            logger.info(f"Successfully loaded data from {self.filepath}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {self.filepath}: {str(e)}")
            raise


class HeadingCollector(Treeprocessor):
    def __init__(self, md):
        super().__init__(md)
        self.chunks = []
        self.current_chunk = None

    def run(self, root):
        for element in root:
            if element.tag in ['h1', 'h2']:
                if self.current_chunk:
                    self.chunks.append(self.current_chunk)
                self.current_chunk = {
                    'main_heading': element.text,
                    'content': '',
                    'level': int(element.tag[1])
                }
            elif self.current_chunk is not None:
                self.current_chunk['content'] += markdown.treeprocessors.etree.tostring(element,
                                                                                        encoding='unicode')

        if self.current_chunk:
            self.chunks.append(self.current_chunk)

        return root

class HeadingCollectorExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {}
        super(HeadingCollectorExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        heading_collector = HeadingCollector(md)
        md.treeprocessors.register(heading_collector, 'heading_collector', 15)
        md.heading_collector = heading_collector

class TokenCounter:
    def __init__(self, model_name="cl100k_base"):
        self.encoder = tiktoken.get_encoding(model_name)

    def count_tokens(self, text: str) -> int:
        return len(self.encoder.encode(text))


class ChunkProcessor:
    def __init__(self, token_counter: TokenCounter, min_tokens: int = 800, max_tokens: int = 1200):
        self.token_counter = token_counter
        self.min_tokens = min_tokens
        self.max_tokens = max_tokens

    def process_chunk(chunk: Dict[str, Any], source_url: str) -> Dict[str, Any]:
        return {
            "chunk_id": str(uuid.uuid4()),
            "source_url": source_url,
            "main_heading": chunk['main_heading'],
            "content": chunk['content'].strip(),
            "summary": ""  # Placeholder for summary
        }


def parse_markdown(content: str) -> List[Dict[str, Any]]:
    md = markdown.Markdown(extensions=[HeadingCollectorExtension()])
    md.convert(content)
    return md.heading_collector.chunks


def main():
    filename = "supabase.com_docs__20240826_212435.json"
    data_loader = DataLoader(filename)
    raw_data = data_loader.load_json_data()

    if raw_data['data']:
        first_page = raw_data['data'][0]
        content = first_page.get('markdown', '')
        source_url = first_page.get('metadata', {}).get('sourceURL', 'Unknown URL')

        logger.info(f"Processing page: {source_url}")

        chunks = parse_markdown(content)
        processed_chunks = [ChunkProcessor.process_chunk(chunk, source_url) for chunk in chunks]

        logger.info(f"Total chunks identified: {len(processed_chunks)}")

        # Display the first few chunks for verification
        for i, chunk in enumerate(processed_chunks[:3], 1):
            logger.info(f"\nChunk {i}:")
            logger.info(f"Chunk ID: {chunk['chunk_id']}")
            logger.info(f"Main Heading: {chunk['main_heading']}")
            logger.info(f"Content Preview: {chunk['content'][:100]}...")

        # Save processed chunks to a JSON file
        output_file = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "processed",
                                   "chunked_supabase_docs.json")
        with open(output_file, 'w') as f:
            json.dump(processed_chunks, f, indent=2)
        logger.info(f"Saved processed chunks to {output_file}")

        # Summary stats
        logger.info(f"\nSummary Statistics:")
        logger.info(f"Total number of chunks: {len(processed_chunks)}")
        logger.info(
            f"Average chunk size (characters): {sum(len(chunk['content']) for chunk in processed_chunks) / len(processed_chunks):.2f}")
    else:
        logger.warning("No data found in the input file.")


if __name__ == "__main__":
    main()