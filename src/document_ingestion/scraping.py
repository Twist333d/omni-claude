import os
import json
import time
from datetime import datetime
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
from urllib.parse import urlparse
import signal
import sys
import requests


load_dotenv()


class FirecrawlScraper:
    def __init__(self):
        self.api_key = os.getenv("FIRECRAWL_API_KEY")
        self.app = FirecrawlApp(api_key=self.api_key)
        self.current_job_id = None
        self.interrupt_received = False
        self.api_base_url = "https://api.firecrawl.dev/v0"

    def signal_handler(self, signum, frame):
        print("\nInterrupt received. Cancelling job...")
        self.interrupt_received = True
        if self.current_job_id:
            self.cancel_job(self.current_job_id)

    def cancel_job(self, job_id):
        url = f"{self.api_base_url}/crawl/cancel/{job_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            if result.get('status') == 'cancelled':
                print(f"Job {job_id} cancelled successfully.")
            else:
                print(f"Unexpected response when cancelling job {job_id}: {result}")
        except requests.RequestException as e:
            print(f"Error cancelling job {job_id}: {str(e)}")

    def crawl_url(self, base_url, max_pages):
        params = {
            'crawlerOptions': {
                'includes': [
                    "/en/latest/*",
                ],
                'excludes': [
                    # Add any patterns here you want to exclude, if any
                ],
                'limit': max_pages,
                'maxDepth': 5,
                'allowBackwardCrawling': True,
                'allowExternalContentLinks': False,
            },
            'pageOptions': {
                'onlyMainContent': False # want to get all footers, navi, headers
            }
        }

        print(f"Starting crawl for: {base_url}")
        crawl_result = self.app.crawl_url(base_url, params=params, wait_until_done=False)
        self.current_job_id = crawl_result['jobId']

        print(f"Crawl job started for {base_url}. Job ID: {self.current_job_id}")
        print("Checking status every 5 seconds...")

        while not self.interrupt_received:
            time.sleep(30)
            status = self.app.check_crawl_status(self.current_job_id)
            print(f"Crawl job status: {status['status']} - {status['current']}/{status['total']} pages processed. "
                  f"Re-checking in 30 seconds...")

            if status['status'] == 'completed':
                return status['data']
            if status['status'] == 'failed':
                if self.interrupt_received:
                    print("Crawl job was cancelled.")
                    return None
                else:
                    raise Exception(f"Crawl job failed: {status.get('error', 'Unknown error')}")

        print("Crawl interrupted by user.")
        return None

def save_raw_data(url, data):
    parsed_url = urlparse(url)
    print("Printing parsed url:", parsed_url)
    base_name = parsed_url.netloc + parsed_url.path.replace('/', '_')
    filename = f"data/raw/{base_name}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    content = {
        "base_url": url,
        "timestamp": datetime.now().isoformat(),
        "data": data
    }

    with open(filename, 'w') as f:
        json.dump(content, f, indent=2)

    return filename

def scrape_and_save(base_url, max_pages):
    scraper = FirecrawlScraper()
    signal.signal(signal.SIGINT, scraper.signal_handler)

    raw_data = scraper.crawl_url(base_url, max_pages)
    if raw_data:
        filename = save_raw_data(base_url, raw_data)
        print(f"Crawl completed. Data saved to: {filename}")
        return filename
    else:
        print("Crawl was interrupted. No data saved.")
        return None

def view_results(filename):
    if not filename:
        print("No results to view.")
        return

    with open(filename, 'r') as f:
        crawled_data = json.load(f)

    print(f"\nCrawl Results:")
    print(f"URL: {crawled_data['base_url']}")
    print(f"Timestamp: {crawled_data['timestamp']}")
    print(f"Number of pages crawled: {len(crawled_data['data'])}")

    for i, page in enumerate(crawled_data['data'][:5], 1):  # Display first 5 pages
        print(f"\nPage {i}:")
        print(f"Title: {page['metadata']['title']}")
        print(f"URL: {page['metadata']['sourceURL']}")
        print(f"Markdown preview: {page['markdown'][:200]}...")  # Display first 200 characters of markdown

    if len(crawled_data['data']) > 5:
        print(f"\n... and {len(crawled_data['data']) - 5} more pages")

if __name__ == "__main__":
    base_url = "https://docs.python-telegram-bot.org/"
    result_file = scrape_and_save(base_url, max_pages=25)  # Set max_pages high enough to capture all pages
    view_results(result_file)