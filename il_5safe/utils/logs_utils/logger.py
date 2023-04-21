import logging
from colored_logger import ColoredLogger
from config import LOG_FILE

logger = ColoredLogger("IL-5Safe", "main.py")

file_handler = logging.FileHandler(log_file)
"""
file_handler: logging.FileHandler
    The file handler for the logger object.
"""

file_handler.setLevel(logging.DEBUG)

log_format = logging.Formatter(
    "%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S"
)
"""
log_format: logging.Formatter
    The format for the log messages.
"""

file_handler.setFormatter(log_format)

logger.addHandler(file_handler)
