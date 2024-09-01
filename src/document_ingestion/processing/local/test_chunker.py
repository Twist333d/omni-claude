import json
import os
from tqdm import tqdm

def test_chunker(input_file: str, max_tokens: int = 1000):
    # Assuming InputProcessor is already implemented
    from src.document_ingestion.processing.chunking_new import InputProcessor, Chunker

    processor = InputProcessor(input_file)
    chunker = Chunker(max_tokens=max_tokens)

    try:
        loaded_data = processor.load_json()
        if not processor.validate_input(loaded_data):
            raise ValueError("Input data structure is invalid")

        all_chunks = []
        total_pages = len(loaded_data['data'])
        total_chunks = 0
        total_tokens = 0

        for i, page in enumerate(tqdm(loaded_data['data'], desc="Processing pages")):
            markdown_content = page['markdown']
            source_url = page['metadata']['sourceURL']

            chunks = chunker.parse_markdown(markdown_content, source_url)
            all_chunks.extend(chunks)
            total_chunks += len(chunks)
            total_tokens += sum(chunk['token_count'] for chunk in chunks)

        # Log full chunk content to a file
        log_file = 'chunking_log.txt'
        with open(log_file, 'w', encoding='utf-8') as f:
            for chunk in all_chunks:
                f.write(f"Chunk ID: {chunk['chunk_id']}\n")
                f.write(f"Source URL: {chunk['source_url']}\n")
                f.write(f"Metadata: {json.dumps(chunk['metadata'], indent=2)}\n")
                f.write(f"Token Count: {chunk['token_count']}\n")
                f.write(f"Has Code Block: {chunk['has_code_block']}\n")
                f.write(f"Oversized Code Block: {chunk['oversized_code_block']}\n")
                f.write(f"Content:\n{chunk['content']}\n\n")
                f.write("-" * 80 + "\n\n")

        # Print summary statistics
        print(f"\nTotal Pages Processed: {total_pages}")
        print(f"Total Chunks Created: {total_chunks}")
        print(f"Total Tokens: {total_tokens}")
        print(f"Average Tokens per Chunk: {total_tokens / total_chunks:.2f}")
        print(f"Full chunk content logged to: {log_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "supabase.com_docs__20240826_212435.json"  # Replace with the actual path
    max_tokens = 1000  # Adjust as needed
    test_chunker(input_file, max_tokens)
