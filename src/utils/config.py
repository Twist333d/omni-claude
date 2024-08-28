import os
from dotenv import load_dotenv

load_dotenv()

# FireCrawl Configuration
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
FIRECRAWL_API_URL = "https://api.firecrawl.dev/v0"

# Anthropic Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")



# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
JOB_FILE_DIR = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "jobs")
JOB_FILE_PATH = os.path.join(JOB_FILE_DIR, "jobs.json")
RAW_DATA_DIR = os.path.join(BASE_DIR, "src", "document_ingestion", "data", "raw")

# Ensure directories exist
os.makedirs(JOB_FILE_DIR, exist_ok=True)
os.makedirs(RAW_DATA_DIR, exist_ok=True)