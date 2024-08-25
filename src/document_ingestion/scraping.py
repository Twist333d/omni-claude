import os
import json
import time
from datetime import datetime
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

class FirecrawlScraper:
    def __init__(self, max_pages):
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        self.app = FirecrawlApp(api_key=self.api_key)
        self.max_pages = max_pages

    def crawl_url(self, url):
        params = {
            'crawlerOptions': {
                'limit': self.max_pages,
                'maxDepth': 4,
                "allowBackwardCrawling": True,
            },
            'pageOptions': {
                'onlyMainContent': False # we want the markdown
            }
        }

        print(f"Starting crawl for: {url}")
        crawl_result = self.app.crawl_url(url, params=params, wait_until_done=False)
        job_id = crawl_result['jobId']

        print(f"Crawl job started. Job ID: {job_id}")
        print("Checking status every 5 seconds...")

        while True:
            time.sleep(5)  # Check status every 5 seconds
            status = self.app.check_crawl_status(job_id)
            print(f"Crawl job status: {status['status']} - {status['current']}/{status['total']} pages processed. "
                  f"Re-checking status every 5 seconds...")

            if status['status'] == 'completed':
                return status['data']
            elif status['status'] == 'failed':
                raise Exception(f"Crawl job failed: {status.get('error', 'Unknown error')}")

def save_raw_data(url, data):
    parsed_url = urlparse(url)
    base_name = parsed_url.netloc + parsed_url.path.replace('/', '_')
    filename = f"data/raw/{base_name}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    content = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "data": data
    }

    with open(filename, 'w') as f:
        json.dump(content, f, indent=2)

    return filename

def scrape_and_save(url, max_pages):
    scraper = FirecrawlScraper(max_pages=max_pages)
    raw_data = scraper.crawl_url(url)
    filename = save_raw_data(url, raw_data)
    print(f"Crawl completed. Data saved to: {filename}")
    return filename

def view_results(filename):
    with open(filename, 'r') as f:
        crawled_data = json.load(f)

    print(f"\nCrawl Results:")
    print(f"URL: {crawled_data['url']}")
    print(f"Timestamp: {crawled_data['timestamp']}")
    print(f"Number of pages crawled: {len(crawled_data['data'])}")

    for i, page in enumerate(crawled_data['data'][:5], 1):  # Display first 5 pages
        print(f"\nPage {i}:")
        print(f"Title: {page['metadata']['title']}")
        print(f"URL: {page['metadata']['sourceURL']}")
        print(f"Markdown preview: {page['markdown'][:200]}...")  # Display first 200 characters of markdown

    if len(crawled_data['data']) > 5:
        print(f"\n... and {len(crawled_data['data']) - 5} more pages")

# Test the scraping functionality


# Test the scraping functionality
if __name__ == "__main__":
    test_url = "https://docs.python-telegram-bot.org/en/v21.4/"
    result_file = scrape_and_save(test_url, max_pages=5)
    view_results(result_file)