import os
from datetime import datetime

LOG_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
"""
LOG_FOLDER: str
    The path to the folder where the log file will be saved.
"""

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


log_file = os.path.join(
    LOG_FOLDER, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
)
"""
log_file: str
    The name of the log file, including the current date and time.
"""

CUSTOM_LEVELS = {
    "INFO": {"color": "", "value": 21},
    "SUCCESS": {"color": "\033[32m", "value": 25},
    "WARNING": {"color": "\033[33m", "value": 31},
    "ERROR": {"color": "\033[31m", "value": 41},
    "CRITICAL": {"color": "\033[41m\033[37m", "value": 51},
}
