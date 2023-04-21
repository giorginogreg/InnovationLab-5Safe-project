import logging
from config import CUSTOM_LEVELS


PROJECT_NAME_COLOR = "\033[32m"
FILENAME_COLOR = "\033[36m"

"""
CUSTOM_LEVELS: dict
    A dictionary that maps custom logging level names to their corresponding log level values and colors.
"""

for level_name, level_dict in CUSTOM_LEVELS.items():
    level_value = level_dict["value"]
    level_color = level_dict["color"]
    logging.addLevelName(level_value, level_name)

    def custom_log(self, message, *args, **kwargs):
        """
        A custom log function that adds color to log messages based on their log levels and other attributes.

        Parameters:
        -----------
        self : logging.Logger
            The logger object.
        message : str
            The log message to be logged.
        *args
            Additional positional arguments to be passed to the logger.
        **kwargs
            Additional keyword arguments to be passed to the logger.
        """
        message = f"{PROJECT_NAME_COLOR}{self.project_name}{logging.getLevelName(self.level)}{FILENAME_COLOR}{self.filename}{message}"
        message += "\033[0m"
        self.log(level_value, message, *args, **kwargs)

    logging.Logger.makeRecord = custom_log
    logging.addLevelName(level_value, level_name)


class ColoredLogger(logging.Logger):
    """
    A custom logger class that adds color to log messages based on their log levels and other attributes.

    Attributes:
    -----------
    project_name : str
        The name of the project being logged.
    filename : str
        The name of the file being logged.
    level : int
        The logging level to be used by the logger.

    Methods:
    --------
    success(msg, *args, **kwargs):
        Logs a message with log level SUCCESS (25). Used to indicate a successful operation.
    warning(msg, *args, **kwargs):
        Logs a message with log level WARNING (31). Used to indicate a potential issue that may not be critical.
    error(msg, *args, **kwargs):
        Logs a message with log level ERROR (41). Used to indicate a critical error that has occurred.
    critical(msg, *args, **kwargs):
        Logs a message with log level CRITICAL (51). Used to indicate a severe error that has caused the program to halt.

    Examples:
    ---------
    logger = ColoredLogger('project_name', 'main.py')
    logger.success('Task completed successfully.')
    logger.warning('Invalid input received.')
    logger.error('Failed to connect to database.')
    logger.critical('Unrecoverable error occurred.')
    """

    def __init__(self, project_name, filename, level=logging.DEBUG):
        """
        Initializes the ColoredLogger object.

        Parameters:
        -----------
        project_name : str
            The name of the project being logged.
        filename : str
            The name of the file being logged.
        level : int, optional
            The logging level to be used by the logger. Default is logging.DEBUG.
        """
        super().__init__(project_name)
        self.project_name = project_name
        self.filename = filename
        self.setLevel(level)

    def success(self, msg, *args, **kwargs):
        """
        Logs a message with log level SUCCESS (25). Used to indicate a successful operation.

        Parameters:
        -----------
        msg : str
            The message to be logged.
        *args : tuple
            Optional positional arguments to be passed to the logging function.
        **kwargs : dict
            Optional keyword arguments to be passed to the logging function.
        """
        self.log(25, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Logs a message with log level WARNING (31). Used to indicate a potential issue that may not be critical.

        Parameters:
        -----------
        msg : str
            The message to be logged.
        *args : tuple
            Optional positional arguments to be passed to the logging function.
        **kwargs : dict
            Optional keyword arguments to be passed to the logging function.
        """
        self.log(31, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Logs a message with log level ERROR (41). Used to indicate a critical error that has occurred.

        Parameters:
        -----------
        msg : str
            The message to be logged.
        *args : tuple
            Optional positional arguments to be passed to the logging function.
        **kwargs : dict
            Optional keyword arguments to be passed to the logging function.
        """
        self.log(41, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Logs a message with log level CRITICAL (51). Used to indicate a severe error that has caused the program to halt.

        Parameters:
        -----------
        msg : str
            The message to be logged.
        *args : tuple
            Optional positional arguments to be passed to the logging function.
        **kwargs : dict
            Optional keyword arguments to be passed to the logging function.
        """
        self.log(51, msg, *args, **kwargs)
