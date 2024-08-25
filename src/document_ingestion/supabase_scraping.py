import time
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Firecrawl with API key
api_key = os.getenv("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key=api_key)

# Base URL for crawling
base_url = "https://supabase.com/docs/"

# Crawl parameters
params = {
    'crawlerOptions': {
        'includes': [
            "/guides/*",
            "/reference/python/*",
        ],
        'limit': 25,  # Adjust as necessary, currently set low for testing
        'maxDepth': 5,
        'mode' : 'fast',
        'allowBackwardCrawling': True,
        'allowExternalContentLinks': False,
    },
    'pageOptions': {
        'onlyMainContent': True
    }
}

# Start the crawl
print(f"Starting crawl for: {base_url}")
crawl_result = app.crawl_url(base_url, params=params, wait_until_done=False)
job_id = crawl_result['jobId']

print(f"Crawl job started. Job ID: {job_id}")
print("Checking status every 5 seconds...")

# Check status loop
while True:
    time.sleep(5)
    status = app.check_crawl_status(job_id)
    print(f"Crawl job status: {status['status']} - {status['current']}/{status['total']} pages processed. Re-checking in 5 seconds...")

    if status['status'] == 'completed' or status['status'] == 'failed':
        break

print(f"Crawl job ended with status: {status['status']}")