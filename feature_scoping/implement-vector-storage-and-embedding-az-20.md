# Feature
Implementation of Chroma DB and vector embeddings for the chunked docs

# Examples
Example from Anthropic's RAG tutorial:
```python
import os
import pickle
import json
import numpy as np
import voyageai

class VectorDB:
    def __init__(self, name, api_key=None):
        if api_key is None:
            api_key = os.getenv("VOYAGE_API_KEY")
        self.client = voyageai.Client(api_key=api_key)
        self.name = name
        self.embeddings = []
        self.metadata = []
        self.query_cache = {}
        self.db_path = f"./data/{name}/vector_db.pkl"

    def load_data(self, data):
        if self.embeddings and self.metadata:
            print("Vector database is already loaded. Skipping data loading.")
            return
        if os.path.exists(self.db_path):
            print("Loading vector database from disk.")
            self.load_db()
            return

        texts = [f"Heading: {item['chunk_heading']}\n\n Chunk Text:{item['text']}" for item in data]
        self._embed_and_store(texts, data)
        self.save_db()
        print("Vector database loaded and saved.")

    def _embed_and_store(self, texts, data):
        batch_size = 128
        result = [
            self.client.embed(
                texts[i : i + batch_size],
                model="voyage-2"
            ).embeddings
            for i in range(0, len(texts), batch_size)
        ]
        self.embeddings = [embedding for batch in result for embedding in batch]
        self.metadata = data

    def search(self, query, k=5, similarity_threshold=0.75):
        if query in self.query_cache:
            query_embedding = self.query_cache[query]
        else:
            query_embedding = self.client.embed([query], model="voyage-2").embeddings[0]
            self.query_cache[query] = query_embedding

        if not self.embeddings:
            raise ValueError("No data loaded in the vector database.")

        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[::-1]
        top_examples = []
        
        for idx in top_indices:
            if similarities[idx] >= similarity_threshold:
                example = {
                    "metadata": self.metadata[idx],
                    "similarity": similarities[idx],
                }
                top_examples.append(example)
                
                if len(top_examples) >= k:
                    break
        self.save_db()
        return top_examples

    def save_db(self):
        data = {
            "embeddings": self.embeddings,
            "metadata": self.metadata,
            "query_cache": json.dumps(self.query_cache),
        }
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "wb") as file:
            pickle.dump(data, file)

    def load_db(self):
        if not os.path.exists(self.db_path):
            raise ValueError("Vector database file not found. Use load_data to create a new database.")
        with open(self.db_path, "rb") as file:
            data = pickle.load(file)
        self.embeddings = data["embeddings"]
        self.metadata = data["metadata"]
        self.query_cache = json.loads(data["query_cache"])
```

I need to define something similar but using ChromaDB and vector embeddings from OpenAI.

## Scope
- Create a ChromaDB database
- Load chunks into the database
- Generate embeddings using OpenAI's API
- Store data in ChromaDB
- Load the database
- Save the database

## Inputs
- Chunks which have the following structure
- File path (example): src/document_ingestion/data/processed/processed_supabase_docs_20240901_193122.json
```json
{
  "metadata": {
    "input_file": "supabase.com_docs__20240826_212435.json",
    "timestamp": "2024-09-01T19:31:23.720577",
    "total_documents": 25,
    "total_chunks": 2000
  },
  "chunks": [
    {
      "source_url": "https://supabase.com/docs/reference/python/initializing",
      "headers": {
        "H1": ""
      },
      "content": "\nPython Client Library=====================\n\nsupabase-py[View on GitHub](https://github.com/supabase/supabase-py)\n\nThis reference documents every object and method available in Supabase's Python library, [supabase-py](https://github.com/supabase/supabase-py)\n. You can use supabase-py to interact with your Postgres database, listen to database changes, invoke Deno Edge Functions, build login and user management functionality, and manage large files.\n\n* * *\n",
      "chunk_id": "c6b5fde8-d48b-43e8-a77f-04035d1a61f7",
      "token_count": 113,
      "has_code_block": false
    },
    {
      "source_url": "https://supabase.com/docs/reference/python/initializing",
      "headers": {
        "H1": "",
        "H2": "",
        "H3": "Install with PyPi[#](#install-with-pypi)"
      },
      "content": "\nInstalling----------\n\n### Install with PyPi[#](#install-with-pypi)\n\nYou can install supabase-py via the terminal. (for > Python 3.7)\n\nPIPConda\n\nTerminal\n\n`     _10  pip install supabase      `\n\n* * *\n* * *\n",
      "chunk_id": "4585735c-b033-4081-bd39-4969af397174",
      "token_count": 62,
      "has_code_block": false
    },
    {
      "source_url": "https://supabase.com/docs/reference/python/initializing",
      "headers": {
        "H1": "",
        "H2": "",
        "H3": "Parameters"
      },
```
## Outputs

- A ChromaDB instance containing:
  - Document chunks
  - Generated embeddings
  - Associated metadata
- Search functionality to retrieve relevant chunks based on queries

## High-level Approach

1. Set up ChromaDB client
2. Create a collection for storing document chunks
3. Process input JSON file
4. For each chunk:
   - Generate embedding using OpenAI API
   - Add chunk to ChromaDB collection with embedding and metadata
5. Implement search functionality using ChromaDB's query methods
6. Provide methods to save and load the database state

## Component Structure

1. `VectorDB` class:
   - Initialize ChromaDB client and collection
   - Methods:
     - `add_chunks(chunks)`: Add chunks to the database
     - `search(query, filters=None, k=5, similarity_threshold=0.7)`: Perform similarity search with optional filtering
     - `update_chunks(chunks)`: Update existing chunks
     - `delete_chunks(chunk_ids)`: Remove chunks from the database
     - `get_stats()`: Retrieve database statistics

2. `EmbeddingGenerator` class:
   - Interface with OpenAI API
   - Methods:
     - `generate_embeddings(texts)`: Generate embeddings for given texts
     - `generate_query_embedding(query)`: Generate embedding for a search query

3. `ChunkProcessor` class:
   - Process input JSON file
   - Methods:
     - `load_chunks(file_path)`: Load and parse the input JSON file
     - `prepare_chunks(chunks)`: Prepare chunks for insertion into VectorDB
     - `batch_chunks(chunks, batch_size=100)`: Create batches of chunks for processing

4. `QueryCache` class:
   - Manage caching of query embeddings
   - Methods:
     - `get(query)`: Retrieve cached embedding for a query
     - `set(query, embedding)`: Cache embedding for a query
     - `clear()`: Clear the cache

5. `SearchResult` class:
   - Represent and format search results
   - Methods:
     - `format_result(chunk, similarity_score)`: Format a single search result
     - `sort_results(results)`: Sort results by relevance

## Implementation details

### Search Implementation

1. **ChromaDB Search Capabilities**
   - ChromaDB provides built-in similarity search functionality.
   - We'll use the `collection.query()` method for searching.

2. **Search Types to Implement**
   a. **Similarity Search**
      - Use ChromaDB's default cosine similarity search.
      - Implement as the primary search method.

   b. **Metadata Filtering**
      - Utilize ChromaDB's ability to filter results based on metadata.
      - Useful for narrowing search to specific document sections or types.

   c. **Hybrid Search**
      - Combine similarity search with metadata filtering for more precise results.

3. **Search Implementation Details**
   - Convert user query to embedding using OpenAI API.
   - Use `collection.query()` with the query embedding.
   - Implement optional metadata filters in the query.
   - Return top N results based on similarity score.

4. **Advanced Search Features**
   - Implement semantic search using the embeddings.
   - Add support for boolean queries (AND, OR, NOT) using metadata filters.
   - Implement faceted search using metadata fields.

### Data Loading Process

1. **JSON Processing**
   - Use Python's `json` module to load the input JSON file.
   - Extract individual chunks from the loaded data.

2. **Chunk Processing**
   - Create a `ChunkProcessor` class to handle chunk preparation.
   - Extract relevant fields from each chunk (content, metadata, etc.).

3. **Batch Processing**
   - Implement batch processing to handle large datasets efficiently.
   - Define an optimal batch size (e.g., 100 chunks per batch) for embedding generation and database insertion.

4. **Embedding Generation**
   - Use OpenAI's API to generate embeddings for each chunk's content.
   - Implement rate limiting and error handling for API calls.

5. **ChromaDB Insertion**
   - Use `collection.add()` method to insert chunks with their embeddings and metadata.
   - Ensure proper mapping of chunk fields to ChromaDB's expected format.

### Lessons from Anthropic's Example

1. **Query Caching**
   - Implement a query cache similar to Anthropic's example.
   - Store embeddings of previously searched queries to reduce API calls.

2. **Similarity Threshold**
   - Adopt the concept of a similarity threshold for filtering results.
   - Implement as an optional parameter in the search method.

3. **Metadata Handling**
   - Store comprehensive metadata for each chunk, similar to Anthropic's approach.
   - Use metadata for advanced filtering and result presentation.

4. **Persistence**
   - Implement save and load functionality for the database.
   - Use ChromaDB's built-in persistence instead of pickle files.

5. **Batch Embedding Generation**
   - Adopt the batch processing approach for embedding generation.
   - Adjust batch size based on OpenAI API limits and performance testing.

## Edge cases