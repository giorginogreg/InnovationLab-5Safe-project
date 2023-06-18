import os
import logging
import coloredlogs
import time


def setup_logger(log_directory="./logs"):
    # Create the logs directory if it doesn't exist
    os.makedirs(log_directory, exist_ok=True)

    # Set up the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define the log file name with a timestamp
    log_file = os.path.join(
        log_directory, f"log_{time.strftime('%Y%m%d_%H%M%S')}.log"
    )

    # Create a file handler for writing logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler for displaying logs in the console with colors
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define the log message format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_date_format = "%Y-%m-%d %H:%M:%S"
    log_formatter = logging.Formatter(log_format, datefmt=log_date_format)

    # Set the formatter for both handlers
    file_handler.setFormatter(log_formatter)
    console_handler.setFormatter(log_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Apply colored logs to the console handler
    coloredlogs.install(
        level="INFO", logger=logger, fmt=log_format, datefmt=log_date_format
    )

    return logger
