import logging
import sys
import os
from src.utils.config import LOG_DIR

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    if logger.handlers:  # Return existing logger if it's already set up
        return logger

    logger.setLevel(level)

    # File handler
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, log_file))
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # Console handler
    console_formatter = logging.Formatter('[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    return logger