import logging.config
from pathlib import Path

import yaml

LOG_LINE_LENGTH = 80


def configure_logging(log_config_file_path: Path):
    """
    Configures the logging system using the provided log configuration file.

    Args:
        log_config_file_path (Path): The path to the log configuration file.

    Returns:
        None
    """
    with open(log_config_file_path, "r") as f:
        log_config = yaml.safe_load(f)
    logging.config.dictConfig(log_config)


def build_error_msg(msg: str) -> str:
    """
    Wraps error message to help it stand out in the log output.

    Args:
        msg (str): The message to format.

    Returns:
        str: The formatted error message.
    """
    err_msg = "\n\n" + " ERROR ".center(LOG_LINE_LENGTH, "!") + "\n"
    err_msg += msg
    err_msg += "\n" + "!" * LOG_LINE_LENGTH + "\n\n"
    return err_msg


COMPLETED_SUCCESSFULLY_MSG = (
    "\n"
    + "!" * LOG_LINE_LENGTH
    + "\n"
    + "   COMPLETED SUCCESSFULLY   ".center(LOG_LINE_LENGTH, "!")
    + "\n"
    + "!" * LOG_LINE_LENGTH
    + "\n"
)
