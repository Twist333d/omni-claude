import os
from src.vector_database.chroma_db import VectorDB
from src.utils.config import PERSIST_DIRECTORY
from pprint import pprint

from src.utils.logger import setup_logger

logger = setup_logger(__name__, 'chroma_db_test_query')

db = VectorDB(PERSIST_DIRECTORY)
query = "How to upsert data in Supabase?"
results = db.query(
    query_texts=[
        query
    ],
    n_results=3
)
print(f"Printing results for this query: {query}")
pprint(results)
