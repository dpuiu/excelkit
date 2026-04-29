"""Excel file reader module."""
import pandas as pd


def read_excel(file_path: str) -> pd.DataFrame | None:
    """
    Reads an excel file and returns a pandas dataframe.
    
    Args:
        file_path: The path to the excel file.
    
    Returns:
        A pandas dataframe containing the data from the excel file,
        or None if an error occurs.
    """
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"An error occurred while reading the excel file: {e}")
        return None