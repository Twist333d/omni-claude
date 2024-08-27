import json
import os
import re
import uuid
from typing import List, Dict, Any
from src.utils.logger import setup_logger
from src.utils.config import RAW_DATA_DIR, BASE_DIR
import anthropic

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


class ChunkIdentifier:
    def identify_chunks(content: str) -> List[Dict[str, Any]]:
        # Split content at main headings (underlined with dashes) or separators (***)
        chunks = re.split(r'\n([^\n]+)\n-+\n|\n\*\s\*\s\*\n', content)

        processed_chunks = []
        current_chunk = None

        for i, chunk in enumerate(chunks):
            if chunk is None or chunk.strip() == '':
                continue

            if i % 2 == 0 and current_chunk:  # Even indexes contain content
                current_chunk['content'] += chunk
                processed_chunks.append(current_chunk)
                current_chunk = None
            elif i % 2 != 0:  # Odd indexes contain headings
                current_chunk = {
                    'main_heading': chunk.strip(),
                    'content': ''
                }

        # Add the last chunk if it exists
        if current_chunk:
            processed_chunks.append(current_chunk)

        return processed_chunks


class ChunkProcessor:
    def process_chunk(chunk: Dict[str, Any], source_url: str) -> Dict[str, Any]:
        return {
            "chunk_id": str(uuid.uuid4()),
            "source_url": source_url,
            "main_heading": chunk['main_heading'],
            "content": chunk['content'].strip(),
            "summary": ""  # Placeholder for summary
        }

class SummaryGenerator:
    def __init__(self, api_key: str):
        self.client = anthropic.Client(api_key)

    def generate_summary(self, chunk: Dict[str, Any]) -> str:
        prompt = f"Please summarize the following content in 2-3 sentences:\n\n{chunk['content']}"
        response = self.client.completions.create(
            model="claude-3-haiku-20240307",
            prompt=prompt,
            max_tokens_to_sample=250,
            temperature=0
        )
        return response.completion.strip()


def main():
    filename = "supabase.com_docs__20240826_212435.json"
    data_loader = DataLoader(filename)
    raw_data = data_loader.load_json_data()

    if raw_data['data']:
        first_page = raw_data['data'][0]
        content = first_page.get('markdown', '')
        source_url = first_page.get('metadata', {}).get('sourceURL', 'Unknown URL')

        logger.info(f"Processing page: {source_url}")

        chunks = ChunkIdentifier.identify_chunks(content)
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
    else:
        logger.warning("No data found in the input file.")


if __name__ == "__main__":
    main()