"""Utility functions for file management and data manipulation.

This module provides utility functions for copying files and writing
DataFrames to CSV files.

Functions:
- copy_file(source_path, target_path): Copies a file from source_path to
  target_path and logs the file paths.
- write_df_to_csv(df, file_path): Writes a DataFrame to a CSV file.
"""

import shutil
import logging
import pandas as pd
from pathlib import Path
from utility.logging_helper import LOG_LINE_LENGTH

# Set up basic logging configuration
logger = logging.getLogger(__name__)


def copy_file(source_path: Path, target_path: Path):
    """Copy a file from the source path to the target path.

    Args:
        source_path (Path): The path of the source file.
        target_path (Path): The path of the target file.

    Raises:
        Exception: If there is an error while copying the file.
    """
    try:
        shutil.copy2(source_path, target_path)
        msg = "\n".join(
            [
                f"File copied from: {source_path}",
                f"              to: {target_path}",
                "-" * LOG_LINE_LENGTH,
            ]
        )
        logger.info("\n" + msg)
    except Exception as e:
        logger.error(
            f"Failed to copy file from {source_path} to {target_path}: {e}"
        )
        raise e


def write_df_to_csv(df: pd.DataFrame, file_path: Path, **kwargs):
    """
    Writes a DataFrame to a CSV file.

    :param df: The DataFrame to write
    :param file_path: The path to the output CSV file
    """
    try:
        df.to_csv(file_path, **kwargs)
        msg = "\n".join(
            [
                f"DataFrame written to CSV file: {file_path}",
                f"Number of rows: {len(df)}",
                "-" * LOG_LINE_LENGTH,
            ]
        )
        logger.info("\n" + msg)
    except Exception as e:
        logger.error(f"Failed to write DataFrame to CSV file: {e}")
        raise e


def read_csv_to_df(file_path: Path, **kwargs) -> pd.DataFrame:
    """
    Reads a CSV file into a DataFrame.

    args:
        file_path (Path): The path to the input CSV file
    returns:
        pd.DataFrame: The DataFrame read from the CSV file
    """
    try:
        df = pd.read_csv(file_path, **kwargs)

        msg = "\n".join(
            [
                "-" * LOG_LINE_LENGTH,
                f"DataFrame read from CSV file: {file_path}",
                f"Number of rows: {len(df)}",
                "-" * LOG_LINE_LENGTH,
            ]
        )
        logger.info("\n" + msg)
        return df
    except Exception as e:
        logger.error(f"Failed to read DataFrame from CSV file: {e}")
        raise e


def read_excel_to_df(
    file_path: Path, sheet_name: str, all_strings=False
) -> pd.DataFrame:
    """
    Reads an Excel file into a DataFrame.

    args:
        file_path (Path): The path to the input CSV file
    returns:
        pd.DataFrame: The DataFrame read from the CSV file
    """
    try:
        if all_strings:
            df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=str)
        else:
            df = pd.read_excel(file_path, sheet_name=sheet_name)

        msg = "\n".join(
            [
                "-" * LOG_LINE_LENGTH,
                f"DataFrame read from Excel file: {file_path}",
                f"Number of rows: {len(df)}",
                "-" * LOG_LINE_LENGTH,
            ]
        )
        logger.info("\n" + msg)
        return df
    except Exception as e:
        logger.error(f"Failed to read DataFrame from Excel file: {e}")
        raise e


def delete_file(file_path: Path):
    """
    Deletes a file.

    args:
        file_path (Path): The path to the file to delete
    """
    try:
        file_path.unlink()
        msg = "\n".join(
            [
                f"File deleted: {file_path}",
                "-" * LOG_LINE_LENGTH,
            ]
        )
        logger.info("\n" + msg)
    except Exception as e:
        logger.error(f"Failed to delete file: {e}")
        raise e


def delete_files(file_paths: list):
    """
    Deletes a list of files.

    args:
        file_paths (list): A list of file paths to delete
    """
    for file_path in file_paths:
        delete_file(file_path)


if __name__ == "__main__":
    # Example usage

    pass
