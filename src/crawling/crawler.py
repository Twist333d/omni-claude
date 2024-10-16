# TODO: Add a CLI to crawler
# TODO: Improve the process flow
# TODO: Properly handle errors
# TODO: Allow users to retrieve the job results

import json
import os
import re
import time
from datetime import datetime
from typing import Any
from urllib.parse import urlparse
from uuid import uuid4

import requests
from firecrawl import FirecrawlApp
from pydantic import HttpUrl
from requests.exceptions import HTTPError, RequestException
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from src.utils.config import FIRECRAWL_API_KEY, JOB_FILE_DIR, RAW_DATA_DIR, SRC_ROOT
from src.utils.decorators import base_error_handler
from src.utils.logger import configure_logging, get_logger

logger = get_logger()


class FireCrawler:
    def __init__(self, api_key: str, data_dir: str = RAW_DATA_DIR, jobs_dir: str = JOB_FILE_DIR) -> None:
        self.api_key: str = api_key
        self.current_job_id: str
        self.raw_data_dir: str = data_dir
        self.jobs_dir: str = jobs_dir
        self.app = self._initialize_app()

    @base_error_handler
    def _initialize_app(self):
        app = FirecrawlApp(api_key=self.api_key)
        logger.info("FireCrawler app initialized successfully.")
        return app

    @base_error_handler
    def map_url(self, url: HttpUrl) -> dict[str, Any] | None:
        """Input a website and get all the urls on the website - extremely fast"""
        logger.info(f"Mapping URL: {url}")

        site_map = self.app.map_url(url)
        logger.info("Map results received. Attempting to parse the results.")

        # extract links and calculate total
        links = site_map
        total_links = len(links)

        logger.info(f"Total number of links received: {total_links}")

        result = {
            "status": "success",
            "input_url": url,
            "total_links": total_links,
            "links": links,
        }

        self.save_results(result, method="map")

        return result

    @staticmethod
    def is_retryable_error(exception):
        """Return True if the exception is an HTTPError with a status code we want to retry."""
        if isinstance(exception, HTTPError):
            return exception.response.status_code in [429, 500, 502, 503, 504]
        return False

    @retry(
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(HTTPError),
        wait=wait_exponential(multiplier=1, min=30, max=300),
        before_sleep=lambda retry_state: logger.info(
            f"Retryable error occurred. Retrying in {retry_state.next_action.sleep} seconds..."
        ),
    )
    @base_error_handler
    def async_crawl_url(self, urls: list[HttpUrl], page_limit: int = 25) -> dict[str, Any]:
        """
        :param urls: List of URLs to be crawled.
        :type urls: list[HttpUrl]
        :param page_limit: Maximum number of pages to be crawled per URL. Defaults to 25.
        :type page_limit: int
        :return: A dictionary containing the input URLs and the results of the crawl jobs.
        :rtype: dict[str, Any]
        """
        all_results = []

        for url in urls:
            params = {
                "limit": page_limit,
                "maxDepth": 5,
                "includePaths": [],
                "excludePaths": [],
                "scrapeOptions": {
                    "formats": [
                        "markdown",
                    ],
                    "excludeTags": ["img"],  # remove images as OmniClaude doesn't support multi-modal embeddings
                },
            }

            logger.info(f"Starting crawl job for URL: {url} with page limit: {page_limit}")
            try:
                response = self.app.async_crawl_url(url, params)
                crawl_job_id = response["id"]  # return the id from FireCrawl
                logger.info(f"Received job ID: {crawl_job_id}")

                # create a job with this id
                self.create_job(job_id=crawl_job_id, method="crawl", input_url=url)

                # check job status
                job_failed = False
                logger.info("***Polling job status***")
                job_status = self._poll_job_results(crawl_job_id)
                if job_status == "failed":
                    # return {"status": "failed", "job_id": crawl_job_id}
                    logger.warning(f"Job {crawl_job_id} failed. Attempting to retrieve partial results.")
                    job_failed = True

                # get all the results
                crawl_results = self._get_all_crawl_results(crawl_job_id)
                unique_links = self._extract_unique_links(crawl_results)
                logger.info(f"Job {crawl_job_id} results received.")
                logger.info(f"Total data entries: {len(crawl_results)}, Unique links: {len(unique_links)}")

                # save the results
                crawl_results = {
                    "job_failed": job_failed,
                    "input_url": url,
                    "total_pages": len(crawl_results),
                    "unique_links": unique_links,
                    "data": crawl_results,
                }

                self.save_results(crawl_results, method="crawl")

                # complete the job
                self.complete_job(crawl_job_id)
                all_results.append(crawl_results)

            except HTTPError as e:
                logger.warning(f"Received HTTPError while crawling {url}: {e}")
                if self.is_retryable_error(e):
                    raise  # raise to the decorator to handle
                else:
                    logger.error(f"HTTPError occurred while crawling {url}: {e}")
                    # Handle other HTTP errors without retrying
                    continue  # Skip to the next URL

        return {"input_urls": urls, "results": all_results}

    @base_error_handler
    def _poll_job_results(self, job_id: str, attempts=None) -> str:
        while True:
            response = self.check_job_status(job_id)
            job_status = response["status"]

            if job_status in ["completed", "failed"]:
                return job_status

            logger.info(f"Job {job_id} status: {job_status}. Retrying in 30 seconds...")
            time.sleep(30)

    @base_error_handler
    def _get_all_crawl_results(self, job_id: str) -> list[dict[str, Any]]:
        """Fetch all results for a given crawl job, handling pagination"""
        next_url = f"https://api.firecrawl.dev/v1/crawl/{job_id}"
        all_data = []

        while next_url:
            logger.info("Accumulating job results.")
            batch_data, next_url = self._get_next_results(next_url)

            # process the first (or only) batch of data
            all_data.extend(batch_data["data"])

            if not next_url:
                logger.info("No more pages to fetch.")
                break  # exit if no more pages to fetch

        return all_data

    @base_error_handler
    def _get_next_results(self, next_url: HttpUrl) -> tuple[dict[str, Any], str | None]:
        """Retrieves the next batch of the results"""
        max_retries = 15
        backoff_factor = 2

        for attempt in range(max_retries):
            try:
                logger.info(f"Trying to fetch the batch results for {next_url}")
                url = next_url
                headers = {"Authorization": f"Bearer {self.api_key}"}
                response = requests.get(url, headers=headers)

                if response.status_code != 200:
                    logger.warning(f"Received status code {response.status_code} from API.")
                    if attempt == max_retries - 1:
                        logger.error(f"Failed to fetch results after {max_retries} attempts.")
                        break
                    else:
                        wait_time = backoff_factor**attempt
                        logger.warning(
                            f"Request failed with status code {response.status_code}. "
                            f"Retrying in {wait_time} seconds..."
                        )
                        time.sleep(wait_time)
                        continue

                batch_data = response.json()
                next_url = batch_data.get("next")  # if it's missing -> there are no more pages to crawl
                return batch_data, next_url
            except RequestException as e:
                if attempt == max_retries - 1:
                    logger.error(f"Failed to fetch results after {max_retries} attempts: {str(e)}")
                    raise
                else:
                    wait_time = backoff_factor**attempt
                    logger.warning(f"Request failed. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)

        # raise Exception("Failed to fetch results after maximum retries")
        logger.error("Failed to fetch results after maximum retries or received error responses.")
        return {"data": []}, None

    @base_error_handler
    def save_results(self, result: dict[str, Any], method: str) -> None:
        """Takes as an input the results of the job, saves it as a json file in the data directory"""
        filename = self._create_file_name(result["input_url"], method)
        filepath = os.path.join(self.raw_data_dir, filename)

        with open(filepath, "w") as f:
            json.dump(result, f, indent=2)

        # build an example file
        self.build_example_file(filename)

        logger.info(f"Results saved to file: {filepath}")

    @base_error_handler
    def _create_file_name(self, url: HttpUrl, method: str) -> str:
        """Creates a filename based on the bare URL and timestamp"""
        parsed_url = urlparse(url)
        bare_url = parsed_url.netloc + parsed_url.path.rstrip("/")
        bare_url = re.sub(r"[^\w\-]", "_", bare_url)  # Replace non-word chars with underscore
        timestamp = self._get_timestamp()
        return f"{bare_url}_{timestamp}.json"

    @base_error_handler
    def _get_timestamp(self):
        """Returns the current timestamp to be used for saving the results"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @base_error_handler
    def create_job(self, job_id: str, method: str, input_url: HttpUrl) -> None:
        """Creates a job, saving information to jobs.json returned by async_crawl_url method."""
        internal_id = str(uuid4())
        path = os.path.join(self.jobs_dir, "jobs.json")  # path should be src/crawling

        # create job info
        job_info = {
            "internal_id": internal_id,
            "job_id": job_id,
            "input_url": input_url,
            "status": "started",
            "timestamp": self._get_timestamp(),
            "method": method,
        }

        try:
            if os.path.exists(path):
                with open(path) as f:
                    jobs = json.load(f)
            else:
                jobs = {}

            # add a new jobs info
            jobs[internal_id] = job_info

            # write updated file to disk
            with open(path, "w") as f:
                json.dump(jobs, f, indent=2)

            # update current job id
            self.current_job_id = internal_id

            logger.info(f"Created a job with firecrawl id: {job_id} and internal_id: {internal_id}")
        except OSError as e:
            logger.error(f"Error saving {job_id}: {e}")
            raise

    @base_error_handler
    def complete_job(self, job_id: str) -> None:
        """Finds a job by external id and updates it's status to "completed"."""
        jobs_path = os.path.join(self.jobs_dir, "jobs.json")

        try:
            with open(jobs_path) as f:
                jobs = json.load(f)

            job_updated = False
            for _internal_id, job_info in jobs.items():
                if job_info["job_id"] == job_id:
                    job_info["status"] = "completed"
                    job_updated = True
                    break

            if not job_updated:
                raise ValueError(f"No job with id {job_id} found")

            with open(jobs_path, "w") as f:
                json.dump(jobs, f, indent=2)

            logger.info(f"Job {job_id} marked as completed.")
        except OSError as e:
            logger.error(f"Error marking job {job_id} as completed: {e}")
            raise

    @base_error_handler
    def check_job_status(self, job_id: str) -> dict[str, Any]:
        """Polls firecrawl for the job result"""
        response = self.app.check_crawl_status(job_id)
        logger.info(
            f"Job {job_id} status: {response['status']}."
            f" Completed: {response.get('completed', 'N/A')}/{response.get('total', 'N/A')}"
        )
        return response

    @base_error_handler
    def _extract_unique_links(self, crawl_results: list[dict[str, Any]]) -> list[str]:
        """Extracts unique links in the completed crawl"""
        unique_links = {
            item["metadata"]["sourceURL"]
            for item in crawl_results
            if "metadata" in item and "sourceURL" in item["metadata"]
        }
        return list(unique_links)

    @base_error_handler
    def build_example_file(self, filename: str, pages: int = 1) -> None:
        """Extracts n pages into example file to visualize its structure"""
        input_filename = filename
        input_filepath = os.path.join(self.raw_data_dir, input_filename)

        md_output_filename = "example.md"
        md_output_filepath = os.path.join(SRC_ROOT, "data", "example", md_output_filename)

        # ensure directory exists
        os.makedirs(os.path.dirname(md_output_filepath), exist_ok=True)

        with open(input_filepath) as f:
            json_data = json.load(f)

        with open(md_output_filepath, "w", encoding="utf-8") as md_file:
            for index, item in enumerate(json_data["data"]):
                if index >= pages:
                    break

                # Markdown file
                if "markdown" in item:
                    md_file.write(f"# Content for item {index}\n\n")
                    md_file.write(f"```markdown\n{item['markdown']}\n```\n\n")
                    md_file.write("----\n\n")

        logger.info(f"Example Markdown file created: {md_output_filepath}")


# Test usage
def main():
    configure_logging(debug=True)
    crawler = FireCrawler(FIRECRAWL_API_KEY)

    # Crawling documentation
    urls_to_crawl = [
        "https://docs.ragas.io/en/stable/",  # replace this
    ]
    crawler.async_crawl_url(urls_to_crawl, page_limit=50)


if __name__ == "__main__":
    main()
