import json
import os
import uuid
from typing import List, Dict, Any
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_DIR, BASE_DIR
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
        self.h1_count = 0
        self.h2_count = 0
        self.h3_count = 0

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
                if element.tag == 'h1':
                    self.h1_count += 1
                else:
                    self.h2_count += 1
            elif element.tag == 'h3':
                self.h3_count += 1
                if self.current_chunk is not None:
                    self.current_chunk['content'] += markdown.treeprocessors.etree.tostring(element, encoding='unicode')
            elif self.current_chunk is not None:
                self.current_chunk['content'] += markdown.treeprocessors.etree.tostring(element, encoding='unicode')

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

    def process_chunk(self, chunk: Dict[str, Any], source_url: str) -> List[Dict[str, Any]]:
        processed_chunk = {
            "chunk_id": str(uuid.uuid4()),
            "source_url": source_url,
            "main_heading": chunk['main_heading'],
            "content": chunk['content'].strip(),
            "summary": ""  # Placeholder for summary
        }

        token_count = self.token_counter.count_tokens(processed_chunk['content'])

        if token_count > self.max_tokens:
            return self.split_large_chunk(processed_chunk)

        return [processed_chunk]

    def split_large_chunk(self, chunk: Dict[str, Any]) -> List[Dict[str, Any]]:
        content = chunk['content']
        splits = []
        current_content = ""
        sentences = content.split('. ')

        for sentence in sentences:
            if self.token_counter.count_tokens(current_content + sentence) > self.max_tokens:
                if current_content:
                    splits.append(current_content.strip())
                    current_content = sentence + '. '
                else:
                    splits.append(sentence.strip())
            else:
                current_content += sentence + '. '

        if current_content:
            splits.append(current_content.strip())

        return [
            {
                "chunk_id": str(uuid.uuid4()),
                "source_url": chunk['source_url'],
                "main_heading": f"{chunk['main_heading']} (Part {i + 1})",
                "content": split_content,
                "summary": ""
            }
            for i, split_content in enumerate(splits)
        ]


def parse_markdown(content: str) -> List[Dict[str, Any]]:
    md = markdown.Markdown(extensions=[HeadingCollectorExtension()])
    md.convert(content)
    return md.heading_collector.chunks


class Validator:
    def validate_chunk_structure(chunk: Dict[str, Any]) -> bool:
        required_keys = ['chunk_id', 'source_url', 'main_heading', 'content', 'summary']
        return all(key in chunk for key in required_keys)

    def validate_completeness(original_content: str, processed_chunks: List[Dict[str, Any]],
                              heading_counts: Dict[str, int]) -> bool:
        original_h1h2_count = heading_counts['h1'] + heading_counts['h2']
        processed_h1h2_count = len(processed_chunks)

        if original_h1h2_count != processed_h1h2_count:
            logger.error(
                f"Mismatch in h1 and h2 headings. Original: {original_h1h2_count}, Processed: {processed_h1h2_count}")
            return False

        original_content_length = len(original_content)
        processed_content_length = sum(len(chunk['content']) for chunk in processed_chunks)

        # Allow for some small difference (e.g., 5%) due to parsing
        if abs(original_content_length - processed_content_length) / original_content_length > 0.05:
            logger.warning(
                f"Significant content length mismatch. Original: {original_content_length}, Processed: {processed_content_length}")

        return True


def main():
    filename = "supabase.com_docs__20240826_212435.json"
    data_loader = DataLoader(filename)
    raw_data = data_loader.load_json_data()

    token_counter = TokenCounter()
    chunk_processor = ChunkProcessor(token_counter)
    all_processed_chunks = []
    total_h1_count = 0
    total_h2_count = 0
    total_h3_count = 0

    for page in raw_data['data']:
        content = page.get('markdown', '')
        source_url = page.get('metadata', {}).get('sourceURL', 'Unknown URL')

        logger.info(f"Processing page: {source_url}")

        md = markdown.Markdown(extensions=[HeadingCollectorExtension()])
        md.convert(content)
        chunks = md.heading_collector.chunks
        total_h1_count += md.heading_collector.h1_count
        total_h2_count += md.heading_collector.h2_count
        total_h3_count += md.heading_collector.h3_count

        processed_chunks = []
        for chunk in chunks:
            processed_chunks.extend(chunk_processor.process_chunk(chunk, source_url))

        all_processed_chunks.extend(processed_chunks)

        # Validate output
        if not Validator.validate_completeness(content, processed_chunks,
                                               {'h1': md.heading_collector.h1_count,
                                                'h2': md.heading_collector.h2_count}):
            logger.error(f"Validation failed for page: {source_url}")

        for chunk in processed_chunks:
            if not Validator.validate_chunk_structure(chunk):
                logger.error(f"Invalid chunk structure for chunk: {chunk['chunk_id']}")

    # Save processed chunks to a JSON file
    output_file = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "processed",
                               "chunked_supabase_docs.json")
    with open(output_file, 'w') as f:
        json.dump(all_processed_chunks, f, indent=2)
    logger.info(f"Saved processed chunks to {output_file}")

    # Enhanced summary statistics
    chunk_sizes = [len(chunk['content']) for chunk in all_processed_chunks]
    token_counts = [token_counter.count_tokens(chunk['content']) for chunk in all_processed_chunks]

    logger.info(f"\nSummary Statistics:")
    logger.info(f"Total number of chunks: {len(all_processed_chunks)}")
    logger.info(f"Total h1 headings: {total_h1_count}")
    logger.info(f"Total h2 headings: {total_h2_count}")
    logger.info(f"Total h3 headings: {total_h3_count}")
    logger.info(f"Average chunk size (characters): {sum(chunk_sizes) / len(chunk_sizes):.2f}")
    logger.info(f"Min chunk size (characters): {min(chunk_sizes)}")
    logger.info(f"Max chunk size (characters): {max(chunk_sizes)}")
    logger.info(f"Average token count per chunk: {sum(token_counts) / len(token_counts):.2f}")
    logger.info(f"Min token count: {min(token_counts)}")
    logger.info(f"Max token count: {max(token_counts)}")

    # Distribution of chunk sizes
    size_ranges = [(0, 500), (501, 1000), (1001, 1500), (1501, 2000), (2001, float('inf'))]
    size_distribution = {f"{start}-{end}": sum(start <= size < end for size in chunk_sizes) for start, end in size_ranges}
    logger.info("Chunk size distribution:")
    for range_str, count in size_distribution.items():
        logger.info(f"  {range_str} characters: {count} chunks")

if __name__ == "__main__":
    main()