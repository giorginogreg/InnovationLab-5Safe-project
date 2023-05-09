import logging
import coloredlogs
from .config import CUSTOM_LEVELS


class ColoredLogger(logging.Logger):
    """
    A custom logger class that adds color to log messages based on their log levels and other attributes.
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
        self._configure_custom_levels()
        self._configure_console_handler()

    def _configure_custom_levels(self):
        """
        Configures the custom log levels.

        This method iterates over the CUSTOM_LEVELS dictionary and adds the custom log level names
        with their corresponding log level values to the logging system.
        """
        for level_name, level_dict in CUSTOM_LEVELS.items():
            level_value = level_dict["value"]
            logging.addLevelName(level_value, level_name)

    def _configure_console_handler(self):
        coloredlogs.install(
            level=self.level,
            logger=self,
            fmt="%(message)s",
            level_styles=coloredlogs.DEFAULT_LEVEL_STYLES,
        )

    def success(self, msg, *args, **kwargs):
        """
        Logs a message with log level SUCCESS (25) and colors.

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
        Logs a message with log level WARNING (31) and colors.

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
