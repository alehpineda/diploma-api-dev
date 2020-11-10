import sys
import logging

from logging.handlers import RotatingFileHandler
from logging import Logger


DEFAULT_FORMAT = "%(asctime)s|%(levelname)s|%(name)s|%(funcName)s|%(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
FILE_SIZE = 1000000
LOG_FILE = "logger.log"


def get_logger(
    log_file: str = LOG_FILE,
    log_level: int = logging.INFO,
    console_level: int = logging.INFO,
    log_format: str = DEFAULT_FORMAT,
    log_name: str = None,
    log_file_flag: bool = False,
    log_stream_flag: bool = True
) -> Logger:
    """
    Creates a new logger and sets handlers and formatting

    """
    # Start new logger
    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    # Time format
    log_format = logging.Formatter(log_format, DATE_FORMAT)
    if log_file_flag:
        # File handler
        file_handler = RotatingFileHandler(log_file, maxBytes=FILE_SIZE)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    if log_stream_flag:
        # Stream handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(console_level)
        stream_handler.setFormatter(log_format)
        logger.addHandler(stream_handler)

    return logger


def change_logger_location(logger: Logger, new_file: str):
    """
    Change logger file path from existing logger
    """
    # New file handler for new log
    new_file_handler = RotatingFileHandler(new_file, maxBytes=FILE_SIZE)
    # Keep formatter and log level
    new_file_handler.setFormatter(logger.handlers[0].formatter)
    new_file_handler.setLevel(logger.getEffectiveLevel())
    # Set handlers
    logger.handlers = [new_file_handler, logger.handlers[1]]
