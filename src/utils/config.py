import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv("FIRECRAWL_API_KEY")
API_BASE_URL = "https://api.firecrawl.dev/v0"

# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
JOB_FILE_DIR = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "jobs")
JOB_FILE_PATH = os.path.join(JOB_FILE_DIR, "jobs.json")
RAW_DATA_DIR = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "raw")

# Ensure directories exist
os.makedirs(JOB_FILE_DIR, exist_ok=True)
os.makedirs(RAW_DATA_DIR, exist_ok=True)