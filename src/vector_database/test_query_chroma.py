import os
from src.vector_database.chroma_db import VectorDB
from src.utils.config import PERSIST_DIRECTORY

# Configuration
DEFAULT_N_RESULTS = 3


def query_db(query: str, n_results: int = 3):
    db = VectorDB(persist_directory=PERSIST_DIRECTORY)
    results = db.query([query], n_results=n_results)

    print(f"\nQuery: {query}")
    print(f"Top {n_results} results:")

    for i in range(min(n_results, len(results['ids'][0]))):
        chunk_id = results['ids'][0][i]
        score = 1 - results['distances'][0][i]
        content = results['documents'][0][i]
        metadata = results['metadatas'][0][i]

        print(f"\n{i + 1}. Chunk ID: {chunk_id}")
        print(f"   Similarity Score: {score:.3f}")
        print(f"   Source URL: {metadata['source_url']}")
        print(f"   Headers: {metadata['headers']}")
        print(f"   Full content: {content[:700]}...")


def main():
    print("Supabase Documentation Query Tool")
    print("Enter your query or press Enter to use the default query.")
    print("Type 'exit' to quit.")

    while True:
        user_query = input(f"\nEnter your query:").strip()

        if user_query.lower() == 'exit':
            print("Exiting the query tool.")
            break

        n_results = input(f"Number of results to display (default: {DEFAULT_N_RESULTS}): ").strip()
        n_results = int(n_results) if n_results.isdigit() else DEFAULT_N_RESULTS

        query_db(user_query, n_results)


if __name__ == "__main__":
    main()