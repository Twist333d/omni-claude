import json
import os
from typing import List, Dict, Any
from src.utils.config import PROCESSED_DATA_DIR, PERSIST_DIRECTORY, LOG_DIR
from src.utils.logger import setup_logger
from src.vector_database.chroma_db import VectorDB

logger = setup_logger("vector_db_test", os.path.join(LOG_DIR, "vector_db_test.log"))

def load_processed_chunks(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['chunks']

def create_test_chunks() -> List[Dict[str, Any]]:
    return [
        {
            "chunk_id": "test1",
            "source_url": "https://supabase.com/docs/guides/ai/quickstarts/vector-search",
            "headers": {"H1": "AI & Vector", "H2": "Vector search quickstart"},
            "content": "This guide demonstrates how to build an AI-powered search engine using Supabase Vector. We'll use OpenAI's embeddings and PostgreSQL's pgvector extension to build a vector search engine.",
            "token_count": 50,
            "has_code_block": False
        },
        {
            "chunk_id": "test2",
            "source_url": "https://supabase.com/docs/guides/auth/social-login/auth-google",
            "headers": {"H1": "Authentication", "H2": "Google OAuth"},
            "content": "Supabase supports Google OAuth out of the box. This guide demonstrates how to configure Google OAuth for your Supabase project and implement 'Sign in with Google' in your app.",
            "token_count": 45,
            "has_code_block": False
        },
        {
            "chunk_id": "test3",
            "source_url": "https://supabase.com/docs/guides/database/extensions/pgcrypto",
            "headers": {"H1": "Database", "H2": "pgcrypto"},
            "content": "pgcrypto is a PostgreSQL extension that provides cryptographic functions. This guide shows how to enable and use pgcrypto in your Supabase project for data encryption and hashing.",
            "token_count": 40,
            "has_code_block": False
        }
    ]


def evaluate_query_results(query: str, results: Dict[str, Any], expected_chunk_id: str = None):
    most_similar_chunk = results['ids'][0][0]
    similarity_score = 1 - results['distances'][0][0]
    is_most_similar = most_similar_chunk == expected_chunk_id if expected_chunk_id else "N/A"

    print(f"\nQuery: {query}")
    print(f"Most similar chunk: {most_similar_chunk}")
    print(f"Similarity score: {similarity_score:.4f}")
    print(f"Is expected most similar: {is_most_similar}")
    print("Top 3 results:")
    for i in range(min(3, len(results['ids'][0]))):
        chunk_id = results['ids'][0][i]
        score = 1 - results['distances'][0][i]
        print(f"  {i + 1}. Chunk: {chunk_id}, Score: {score:.4f}")

def main():
    db = VectorDB(persist_directory=PERSIST_DIRECTORY)
    print("Initialized VectorDB")

    processed_file = os.path.join(PROCESSED_DATA_DIR, "processed_supabase_docs_20240901_193122.json")
    chunks = load_processed_chunks(processed_file)
    print(f"Loaded {len(chunks)} chunks from processed file")

    db.add(chunks)
    print(f"Added {len(chunks)} chunks to VectorDB")

    test_chunks = create_test_chunks()
    db.add(test_chunks)
    print(f"Added {len(test_chunks)} test chunks to VectorDB")

    queries = [
        ("How to implement vector search with Supabase?", "test1"),
        ("Explain Google OAuth integration in Supabase", "test2"),
        ("What is pgcrypto and how to use it in Supabase?", "test3"),
        ("How to initialize Supabase client in Python?", None),
        ("Explain the process of querying data using Supabase Python library", None),
        ("What's the method for inserting data in Supabase using Python?", None),
        ("Describe authentication methods in Supabase Python SDK", None),
        ("How to handle real-time updates with Supabase Python client?", None)
    ]

    for query, expected_chunk_id in queries:
        results = db.query([query], n_results=3)
        evaluate_query_results(query, results, expected_chunk_id)

    total_docs = db.count()
    print(f"\nTotal documents in VectorDB: {total_docs}")

if __name__ == "__main__":
    main()