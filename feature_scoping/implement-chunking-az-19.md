# Implement chunking

## Feature scope
- Process the input JSON data from FireCrawl
- Break down each page into meaningful chunks
- Generate summaries for each chunk using Claude 3 Haiku
- Output a structured JSON file with chunked and summarized content
- Prepare the output for embedding generation

## Input structure
The input is a JSON file containing scraped data from Supabase documentation. Each entry represents a page and includes:

base_url
timestamp
data (array of page objects)

content (raw HTML)
markdown (Markdown version of the content)
metadata (title, description, URL, etc.)

```json
{
  "base_url": "https://supabase.com/docs/",
  "timestamp": "2024-08-30T07:30:45.664429",
  "data": [
    {
      "content": "[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)\n\n*   [Start](/docs/guides/getting-started)\n    \n*   Products\n*   Build\n*   Reference\n*   Resources\n\n[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)\n\nSearch docs...\n\nK\n\n### Where do I find support?\n\nChoose the support channel relevant for your situation here: [supabase.com/support](https://supabase.com/support)\n\n### How much does it cost?\n\nSelf-hosting Supabase is free. If you wish to use our cloud-platform, we provide [simple, predictable pricing](https://supabase.com/pricing)\n.\n\n### How do I host Supabase?\n\nYou can use the docker compose script [here](https://github.com/supabase/supabase/tree/master/docker)\n, and find detailed instructions [here](/docs/guides/hosting/overview)\n.\n\nSupabase is an amalgamation of open source tools. Some of these tools are made by Supabase (like our [Realtime Server](https://github.com/supabase/realtime)\n), some we support directly (like [PostgREST](http://postgrest.org/en/v7.0.0/)\n), and some are third-party tools (like [KonSupabase is an amalgamation open sourceg](https://github.com/Kong/kong)\n).\n\nAll of the tools we use in Supabase are MIT, Apache 2.0, or PostgreSQL licensed. This is one of the requirements to be considered for the Supabase stack.\n\n### How can you be a Firebase alternative if you're built with a relational database?\n\nWe started Supabase because we love the functionality of Firebase, but we personally experienced the scaling issues that many others experienced. We chose Postgres because it's well-trusted, with phenomenal scalability.\n\nOur goal is to make Postgres as easy to use as Firebase, so that you no longer have to choose between usability and scalability. We're sure that once you start using Postgres, you'll love it more than any other database.\n\n### Do you support `[some other database]`?\n\nWe only support PostgreSQL. It's unlikely we'll ever move away from Postgres; however, you can [vote on a new database](https://github.com/supabase/supabase/discussions/6)\n if you want us to start development.\n\n### Do you have a library for `[some other language]`?\n\nWe officially support [JavaScript](/docs/reference/javascript/installing)\n, [Swift](/docs/reference/swift/installing)\n, and [Flutter](/docs/reference/dart/installing)\n.\n\nYou can find community-supported libraries including Python, C#, PHP, and Ruby in our [GitHub Community](https://github.com/supabase-community)\n, and you can also help us to identify the most popular languages by [voting for a new client library](https://github.com/supabase/supabase/discussions/5)\n.\n\n*   Need some help?\n    \n    [Contact support](https://supabase.com/support)\n    \n*   Latest product updates?\n    \n    [See Changelog](https://supabase.com/changelog)\n    \n*   Something's not right?\n    \n    [Check system status](https://status.supabase.com/)\n    \n\n* * *\n\n[\u00a9 Supabase Inc](https://supabase.com/)\n\u2014[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)\n[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)\n[Open Source](https://supabase.com/open-source)\n[SupaSquad](https://supabase.com/supasquad)\nPrivacy Settings\n\n[GitHub](https://github.com/supabase/supabase)\n[Twitter](https://twitter.com/supabase)\n[Discord](https://discord.supabase.com/)",
      "markdown": "[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)\n\n*   [Start](/docs/guides/getting-started)\n    \n*   Products\n*   Build\n*   Reference\n*   Resources\n\n[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75&dpl=dpl_FamQvESN35BiTrVL2ZnRKQ5butin)DOCS](/docs)\n\nSearch docs...\n\nK\n\n### Where do I find support?\n\nChoose the support channel relevant for your situation here: [supabase.com/support](https://supabase.com/support)\n\n### How much does it cost?\n\nSelf-hosting Supabase is free. If you wish to use our cloud-platform, we provide [simple, predictable pricing](https://supabase.com/pricing)\n.\n\n### How do I host Supabase?\n\nYou can use the docker compose script [here](https://github.com/supabase/supabase/tree/master/docker)\n, and find detailed instructions [here](/docs/guides/hosting/overview)\n.\n\nSupabase is an amalgamation of open source tools. Some of these tools are made by Supabase (like our [Realtime Server](https://github.com/supabase/realtime)\n), some we support directly (like [PostgREST](http://postgrest.org/en/v7.0.0/)\n), and some are third-party tools (like [KonSupabase is an amalgamation open sourceg](https://github.com/Kong/kong)\n).\n\nAll of the tools we use in Supabase are MIT, Apache 2.0, or PostgreSQL licensed. This is one of the requirements to be considered for the Supabase stack.\n\n### How can you be a Firebase alternative if you're built with a relational database?\n\nWe started Supabase because we love the functionality of Firebase, but we personally experienced the scaling issues that many others experienced. We chose Postgres because it's well-trusted, with phenomenal scalability.\n\nOur goal is to make Postgres as easy to use as Firebase, so that you no longer have to choose between usability and scalability. We're sure that once you start using Postgres, you'll love it more than any other database.\n\n### Do you support `[some other database]`?\n\nWe only support PostgreSQL. It's unlikely we'll ever move away from Postgres; however, you can [vote on a new database](https://github.com/supabase/supabase/discussions/6)\n if you want us to start development.\n\n### Do you have a library for `[some other language]`?\n\nWe officially support [JavaScript](/docs/reference/javascript/installing)\n, [Swift](/docs/reference/swift/installing)\n, and [Flutter](/docs/reference/dart/installing)\n.\n\nYou can find community-supported libraries including Python, C#, PHP, and Ruby in our [GitHub Community](https://github.com/supabase-community)\n, and you can also help us to identify the most popular languages by [voting for a new client library](https://github.com/supabase/supabase/discussions/5)\n.\n\n*   Need some help?\n    \n    [Contact support](https://supabase.com/support)\n    \n*   Latest product updates?\n    \n    [See Changelog](https://supabase.com/changelog)\n    \n*   Something's not right?\n    \n    [Check system status](https://status.supabase.com/)\n    \n\n* * *\n\n[\u00a9 Supabase Inc](https://supabase.com/)\n\u2014[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)\n[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)\n[Open Source](https://supabase.com/open-source)\n[SupaSquad](https://supabase.com/supasquad)\nPrivacy Settings\n\n[GitHub](https://github.com/supabase/supabase)\n[Twitter](https://twitter.com/supabase)\n[Discord](https://discord.supabase.com/)",
      "metadata": {
        "title": "Supabase Docs",
        "language": "en",
        "sourceURL": "https://supabase.com/docs/faq",
        "pageStatusCode": 200,
        "ogLocaleAlternate": []
      },
      "linksOnPage": [
        "https://supabase.com/docs",
        "https://supabase.com/docs/guides/getting-started",
        "https://supabase.com/support",
        "https://supabase.com/pricing",
        "https://github.com/supabase/supabase/tree/master/docker",
        "https://supabase.com/docs/guides/hosting/overview",
        "https://github.com/supabase/realtime",
        "http://postgrest.org/en/v7.0.0/",
        "https://github.com/Kong/kong",
        "https://github.com/supabase/supabase/discussions/6",
        "https://supabase.com/docs/reference/javascript/installing",
        "https://supabase.com/docs/reference/swift/installing",
        "https://supabase.com/docs/reference/dart/installing",
        "https://github.com/supabase-community",
        "https://github.com/supabase/supabase/discussions/5",
        "https://supabase.com/changelog",
        "https://status.supabase.com/",
        "https://supabase.com/",
        "https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md",
        "https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md",
        "https://supabase.com/open-source",
        "https://supabase.com/supasquad",
        "https://github.com/supabase/supabase",
        "https://twitter.com/supabase",
        "https://discord.supabase.com/"
      ]
    },
```

## Example RAG from Anthropic RAG tutorial
URL: https://github.com/anthropics/anthropic-cookbook/blob/main/skills/retrieval_augmented_generation/guide.ipynb

### Chunk structure
This is the structure of the docs they used in Anthropic tutorial on RAG.
```json
[
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#get-started",
    "chunk_heading": "Get started",
    "text": "Get started\n\n\nIf you\u2019re new to Claude, start here to learn the essentials and make your first API call.\nIntro to ClaudeExplore Claude\u2019s capabilities and development flow.QuickstartLearn how to make your first API call in minutes.Prompt LibraryExplore example prompts for inspiration.\nIntro to ClaudeExplore Claude\u2019s capabilities and development flow.\n\nIntro to Claude\nExplore Claude\u2019s capabilities and development flow.\nQuickstartLearn how to make your first API call in minutes.\n\nQuickstart\nLearn how to make your first API call in minutes.\nPrompt LibraryExplore example prompts for inspiration.\n\nPrompt Library\nExplore example prompts for inspiration.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#models",
    "chunk_heading": "Models",
    "text": "Models\n\n\nClaude consists of a family of large language models that enable you to balance intelligence, speed, and cost.\n\n\n\n\n\nCompare our state-of-the-art models.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#develop-with-claude",
    "chunk_heading": "Develop with Claude",
    "text": "Develop with Claude\n\n\nAnthropic has best-in-class developer tools to build scalable applications with Claude.\nDeveloper ConsoleEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.API ReferenceExplore, implement, and scale with the Anthropic API and SDKs.Anthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\nDeveloper ConsoleEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.\n\nDeveloper Console\nEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.\nAPI ReferenceExplore, implement, and scale with the Anthropic API and SDKs.\n\nAPI Reference\nExplore, implement, and scale with the Anthropic API and SDKs.\nAnthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\n\nAnthropic Cookbook\nLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#key-capabilities",
    "chunk_heading": "Key capabilities",
    "text": "Key capabilities\n\n\nClaude can assist with many tasks that involve text, code, and images.\nText and code generationSummarize text, answer questions, extract data, translate text, and explain and generate code.VisionProcess and analyze visual input and generate text and code from images.\nText and code generationSummarize text, answer questions, extract data, translate text, and explain and generate code.\n\nText and code generation\nSummarize text, answer questions, extract data, translate text, and explain and generate code.\nVisionProcess and analyze visual input and generate text and code from images.\n\nVision\nProcess and analyze visual input and generate text and code from images.\n"
  },
  {
    "chunk_link": "https://docs.anthropic.com/en/docs/welcome#support",
    "chunk_heading": "Support",
    "text": "Support\n\n\nHelp CenterFind answers to frequently asked account and billing questions.Service StatusCheck the status of Anthropic services.\nHelp CenterFind answers to frequently asked account and billing questions.\n\nHelp Center\nFind answers to frequently asked account and billing questions.\nService StatusCheck the status of Anthropic services.\n\nService Status\nCheck the status of Anthropic services.\nQuickstartxlinkedin\nQuickstart\nxlinkedin\nGet started Models Develop with Claude Key capabilities Support\nGet startedModelsDevelop with ClaudeKey capabilitiesSupport\n"
  },
```

So each chunk has:
- chunk_link -> seems like they broke it by sections.
- chunk_heading -> which seems to be the section name.
- text: text of the chunk

### Embedding approach
```python
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
```

So how did they create each chunk for embeddings:
- they created a list where each chunk had it's heading + text
- then they passed it into the embedding model
- later they added summary of the heading + text and appending 'summary' to the chunk

Final chunk structure is:
```python
summarized_doc = {
    "chunk_link": doc["chunk_link"],
    "chunk_heading": doc["chunk_heading"],
    "text": doc["text"],
    "summary": summary
}
```

Summary was generated by the model using this approach:
```python
def generate_summaries(input_file, output_file):
 
    # Load the original documents
    with open(input_file, 'r') as f:
        docs = json.load(f)

    # Prepare the context about the overall knowledge base
    knowledge_base_context = "This is documentation for Anthropic's, a frontier AI lab building Claude, an LLM that excels at a variety of general purpose tasks. These docs contain model details and documentation on Anthropic's APIs."

    summarized_docs = []

    for doc in tqdm(docs, desc="Generating summaries"):
        prompt = f"""
        You are tasked with creating a short summary of the following content from Anthropic's documentation. 

        Context about the knowledge base:
        {knowledge_base_context}

        Content to summarize:
        Heading: {doc['chunk_heading']}
        {doc['text']}

        Please provide a brief summary of the above content in 2-3 sentences. The summary should capture the key points and be concise. We will be using it as a key part of our search pipeline when answering user queries about this content. 

        Avoid using any preamble whatsoever in your response. Statements such as 'here is the summary' or 'the summary is as follows' are prohibited. You should get straight into the summary itself and be concise. Every word matters.
        """

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=150,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        summary = response.content[0].text.strip()

        summarized_doc = {
            "chunk_link": doc["chunk_link"],
            "chunk_heading": doc["chunk_heading"],
            "text": doc["text"],
            "summary": summary
        }
        summarized_docs.append(summarized_doc)

    # Save the summarized documents to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(summarized_docs, f, indent=2)

    print(f"Summaries generated and saved to {output_file}")

# generate_summaries('data/anthropic_docs.json', 'data/anthropic_summary_indexed_docs.json')
```
Summary increased the key metrics of RAG by either small or medium amount (specifically recall increased from 0.56 
to 0.71)

# Chunking and Processing Approach for Supabase Documentation

## 1. End-to-End Approach

1. **Input Processing**
   - Load JSON data from FireCrawl
   - Extract markdown content and metadata for each page
   - Implement error handling for malformed JSON or missing required fields

2. **Document Parsing**
   - Parse markdown content using a robust Markdown parser (e.g., Python-Markdown)
   - Identify H1, H2, and H3 headings using regular expressions
   - Detect code blocks and other special content (e.g., tables, lists)
   - Preserve original Markdown formatting

3. **Chunking**
   - Generate initial chunks based on heading hierarchy
   - Implement a sliding window approach for chunking to ensure context preservation
   - Split large chunks while respecting content boundaries and code blocks
   - Ensure code blocks are not split across chunks
   - Handle edge cases like inconsistent heading hierarchy and very long sections

4. **Enrichment**
   - Add metadata to each chunk (source URL, headings, etc.)
   - Calculate token count using fast approximation method
   - Generate unique chunk IDs (UUIDs)
   - Preserve original heading structure (H1, H2, H3) for each chunk

5. **Summarization**
   - Generate summaries for each chunk using Claude 3 Haiku
   - Implement asynchronous processing for API calls
   - Use a rate limiter to avoid exceeding API limits
   - Implement retry logic for failed API calls

6. **Output Formatting**
   - Structure chunks and summaries into JSON format
   - Ensure proper escaping of special characters in JSON output
   - Compress output if file size is large

7. **Validation and Reporting**
   - Perform integrity checks on the chunking process
   - Generate and display summary statistics
   - Implement checksums for data integrity verification
- 
## 2. Processing Steps and Data Flow

1. Load JSON from FireCrawl
2. Extract Markdown & Metadata
3. Parse Markdown (multiprocessing)
4. Generate Initial Chunks (multiprocessing)
5. Split Large Chunks (multiprocessing)
6. Enrich Chunks with Metadata (multiprocessing)
7. Generate Summaries (async)
8. Format Output JSON
9. Save Output File
10. Validate Results
11. Display Summary Statistics

## 3. Components, Functions, and Methods

### InputProcessor
- `load_json(file_path: str) -> Dict`
- `extract_markdown(page_data: Dict) -> Tuple[str, Dict]`
- `validate_input(data: Dict) -> bool`

### MarkdownParser
- `parse_markdown(content: str) -> ParsedDocument`
- `identify_headings(parsed_doc: ParsedDocument) -> List[Heading]`
- `detect_code_blocks(parsed_doc: ParsedDocument) -> List[CodeBlock]`
- `detect_special_content(parsed_doc: ParsedDocument) -> List[SpecialContent]`

### Chunker
- `generate_initial_chunks(parsed_doc: ParsedDocument) -> List[Chunk]`
- `split_large_chunks(chunks: List[Chunk], max_tokens: int) -> List[Chunk]`
- `respect_code_blocks(chunk: Chunk, code_blocks: List[CodeBlock]) -> List[Chunk]`
- `sliding_window_chunk(content: str, window_size: int, overlap: int) -> List[Chunk]`

### ChunkEnricher
- `enrich_chunk(chunk: Chunk, metadata: Dict) -> EnrichedChunk`
- `generate_chunk_id() -> str`

### Summarizer
- `generate_summary(chunk: EnrichedChunk) -> str`
- `batch_summarize(chunks: List[EnrichedChunk]) -> List[str]`
- `retry_api_call(func: Callable, max_retries: int, backoff_factor: float) -> Any`

### OutputFormatter
- `format_chunks(chunks: List[EnrichedChunk], summaries: List[str]) -> List[Dict]`
- `save_output(formatted_chunks: List[Dict], file_path: str)`
- `compress_output(data: str) -> bytes`

### Validator
- `validate_token_counts(original_docs: List[str], chunks: List[EnrichedChunk]) -> bool`
- `validate_headings_preserved(original_docs: List[str], chunks: List[EnrichedChunk]) -> bool`
- `validate_chunk_sizes(chunks: List[EnrichedChunk], min_tokens: int, max_tokens: int) -> bool`
- `validate_code_block_integrity(original_docs: List[str], chunks: List[EnrichedChunk]) -> bool`
- `calculate_checksum(data: str) -> str`

### StatisticsGenerator
- `generate_statistics(original_docs: List[str], chunks: List[EnrichedChunk]) -> Dict`
- `calculate_token_distribution(chunks: List[EnrichedChunk]) -> Dict`

### Orchestrator
- `run(input_file: str, output_file: str)`
- `process_documents(docs: List[Dict]) -> List[EnrichedChunk]`
- `summarize_chunks(chunks: List[EnrichedChunk]) -> List[str]`
- `validate_and_report(original_docs: List[str], chunks: List[EnrichedChunk])`

## 4. Scalability Considerations

- Implement comprehensive multiprocessing for all CPU-bound tasks
- Use async/await for I/O-bound operations (e.g., API calls for summarization)
- Implement a fast token counting proxy
- Use generators for memory-efficient processing of large datasets
- Implement progress bars and summary statistics for user feedback
- Use batch processing for large datasets that don't fit in memory

### Token Counting Proxy

Implement a fast token counting proxy that provides a good approximation without the computational cost of tiktoken. This method splits on whitespace and punctuation, and adjusts for common subword tokenization patterns.

### Multiprocessing Implementation

Use Python's \`multiprocessing\` module to parallelize CPU-bound tasks. The \`Orchestrator\` class will manage the distribution of work across available CPU cores.

### Asynchronous Summarization

Implement asynchronous processing for API calls to Claude 3 Haiku for summary generation. This allows for concurrent API calls, significantly reducing the overall time for summarization.

## 5. CLI Approach for Main Orchestrator

Implement a command-line interface for the main orchestrator, allowing users to specify input and output files, as well as optional parameters like maximum tokens per chunk and summary length.

## 6. Validator Integration with Orchestrator

The validator is integrated directly into the Orchestrator's workflow. It performs various checks after processing and provides a detailed report to the user.

## 7. Summary Generator Output

The StatisticsGenerator provides comprehensive statistics about the chunking process, including:
- Original document count and token count
- Unique URLs processed
- Total chunks generated
- Token count statistics (total, average, min, max)
- Heading counts (H1, H2)
- Number of chunks with code blocks
- Identified issues (e.g., chunks outside the desired token range)

## 8. Progress Tracking and User Feedback

Implement progress bars using the \`tqdm\` library to provide real-time feedback on:
- Document processing progress
- Summary generation progress

Display summary statistics and validation results at the end of the process.

## 9. Error Handling and Logging

Implement comprehensive error handling and logging throughout the pipeline to catch and report any issues during processing.

## 10. Extensibility

Design the system with extensibility in mind, allowing for easy addition of new features or modifications to existing components without major refactoring.

This approach provides a scalable, efficient, and user-friendly solution for processing and chunking Supabase documentation. It leverages multiprocessing for CPU-bound tasks, asynchronous programming for I/O-bound operations, and provides clear progress indicators and summary statistics to the user. The modular design allows for easy modifications and extensions as needed, making it capable of handling large volumes of documentation efficiently.

## 11. Target Chunk Structure

Each chunk will be structured as follows:

```json
{
  "chunk_id": "unique_identifier",
  "source_url": "https://supabase.com/docs/path/to/page",
  "h1": "Main heading (H1) text",
  "h2": "Subheading (H2) text",
  "h3": "Tertiary heading (H3) text, if applicable",
  "content": "Full content of the chunk, including lower-level headings and all markdown formatting",
  "token_count": 950,
  "summary": "Brief summary generated by Claude 3 Haiku"
}
```
- chunk_id: A unique identifier for the chunk (e.g., UUID)
- source_url: The URL of the original document
- h1, h2, h3: The text of the nearest preceding headings of each level
- content: The full markdown content of the chunk
- token_count: The approximate number of tokens in the content
- summary: A brief summary of the chunk's content

## 12. Handling Edge Cases and Varying Document Structures

To handle edge cases and documents with different structures, we'll implement the following strategies:

1. **Inconsistent Heading Hierarchy**:
   - If a document doesn't start with an H1, use the document title or first heading as H1
   - If H2 appears before H1, treat it as an H1 until a true H1 is encountered
   - Handle missing intermediate levels (e.g., H1 followed directly by H3)

2. **No Clear Headings**:
   - For documents with no clear heading structure, create chunks based on paragraph breaks or a maximum token count
   - Use the document title or first sentence as the H1 for all chunks

3. **Very Short Documents**:
   - If a document is shorter than the minimum chunk size, keep it as a single chunk
   - Add a note in the metadata indicating it's a full document

4. **Very Long Sections**:
   - If content between headings exceeds the maximum chunk size, split it into multiple chunks
   - Maintain the same heading information for all resulting chunks, but add a part number (e.g., "Part 1", "Part 2")

5. **Complex Nested Structures**:
   - Handle nested lists, tables, and other complex markdown structures by keeping them intact within chunks
   - If a complex structure exceeds the maximum chunk size, split at the highest possible level to maintain coherence

6. **Code Blocks**:
   - Never split within a code block
   - If a code block exceeds the maximum chunk size, keep it as a single oversized chunk and flag it in the metadata

7. **Non-Standard Markdown**:
   - Implement a fallback parsing method for documents that don't follow standard markdown conventions
   - This could involve splitting based on line breaks and common formatting patterns

8. **Handling Special Characters and Unicode**:
   - Ensure the parser and token counter can handle special characters, emojis, and various Unicode scripts
   - Implement proper escaping and encoding in the output JSON

9. **Metadata Inconsistencies**:
   - If expected metadata (e.g., source URL) is missing, use placeholder values and flag in the chunk metadata

10. **Varying Content Types**:
    - Be prepared to handle different types of content that might appear in the documentation (e.g., warnings, notes, examples)
    - Develop specific rules for chunking these special content types if necessary

Implementation Details:

- Enhance the \`MarkdownParser\` class to detect and handle these edge cases
- Implement a \`ChunkStrategy\` interface with multiple implementations for different document structures
- Use a \`ChunkStrategyFactory\` to select the appropriate strategy based on document analysis
- Add metadata fields to the chunk structure to flag special handling or potential issues
- Implement comprehensive logging to track how edge cases are handled
- Extend the \`Validator\` to check for and report on unusual chunk structures or content

By implementing these strategies, the chunking process will be more robust and capable of handling a wide variety of document structures and edge cases while still producing consistent and useful chunks for further processing.