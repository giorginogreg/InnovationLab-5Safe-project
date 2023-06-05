import logging
import shutil
import pytest
import os
from typing import Generator

from il_5safe.logs_utils.colored_logger import setup_logger


@pytest.fixture
def temp_logs_directory(tmpdir) -> Generator[str, None, None]:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Create a temporary logs directory
    logs_directory = str(tmpdir.mkdir("logs"))
    yield logs_directory
    # Clean up the temporary logs directory
    shutil.rmtree(logs_directory)


def test_setup_logger(temp_logs_directory: str):
    # Call the setup_logger function with the temporary logs directory
    logger = setup_logger(log_directory=temp_logs_directory)

    # Test if the logger has been created
    assert isinstance(logger, logging.Logger)

    # Test if the log file has been created
    log_files = os.listdir(temp_logs_directory)
    assert len(log_files) == 1
    assert log_files[0].startswith("log_") and log_files[0].endswith(".log")

    # Test if the logger has the expected handlers
    assert len(logger.handlers) == 2
    assert isinstance(logger.handlers[0], logging.FileHandler)
    assert isinstance(logger.handlers[1], logging.StreamHandler)

    # Test if the log level is set correctly
    assert logger.level == logging.DEBUG

    # Test if the log message format is set correctly
    assert isinstance(logger.handlers[0].formatter, logging.Formatter)
    assert isinstance(logger.handlers[1].formatter, logging.Formatter)

    # Test if the log directory exists
    assert os.path.exists(temp_logs_directory) and os.path.isdir(
        temp_logs_directory
    )
