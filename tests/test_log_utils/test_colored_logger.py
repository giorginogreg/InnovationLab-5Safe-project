from io import StringIO
import logging
import pytest
from il_5safe.logs_utils.colored_logger import ColoredLogger


from typing import Tuple


@pytest.fixture
def colored_logger() -> ColoredLogger:
    logger = ColoredLogger("il_5safe", "main.py")
    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    logger.addHandler(console_handler)
    yield logger


@pytest.mark.parametrize(
    "level, expected_level",
    [
        (logging.DEBUG, 10),
        (logging.INFO, 20),
        (logging.WARNING, 30),
        (logging.ERROR, 40),
        (logging.CRITICAL, 50),
    ],
)
def test_level(
    colored_logger: ColoredLogger, level: int, expected_level: int
) -> None:
    colored_logger.setLevel(level)
    assert colored_logger.level == expected_level


def test_success(
    colored_logger: ColoredLogger, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.INFO)
    colored_logger.success("Task completed successfully.")
    assert "Task completed successfully." in caplog.text
    assert caplog.records[0].levelno == logging.INFO


def test_warning(
    colored_logger: ColoredLogger, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.WARNING)
    colored_logger.warning("Invalid input received.")
    assert "Invalid input received." in caplog.text
    assert caplog.records[0].levelno == logging.WARNING


def test_error(
    colored_logger: ColoredLogger, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.ERROR)
    colored_logger.error("Failed to connect to database.")
    assert "Failed to connect to database." in caplog.text
    assert caplog.records[0].levelno == logging.ERROR


def test_critical(
    colored_logger: ColoredLogger, caplog: pytest.LogCaptureFixture
) -> None:
    caplog.set_level(logging.CRITICAL)
    colored_logger.critical("Unrecoverable error occurred.")
    assert "Unrecoverable error occurred." in caplog.text
    assert caplog.records[0].levelno == logging.CRITICAL


def test_format_message(colored_logger: ColoredLogger) -> None:
    colored_logger.level = logging.WARNING
    message = colored_logger._format_message("Test message")
    expected_message = (
        "\033[32mproject_nameWARNING\033[36mmain.pyTest message\033[0m"
    )
    assert message == expected_message
