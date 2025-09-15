# src/hours_file.py
import pandas as pd

def load_hours(path: str) -> pd.DatetimeIndex:
    """
    Read a text file where each line is a valid timestamp.
    Convert all to UTC and round down to the nearest hour.
    Return as a DatetimeIndex.
    """
    s = pd.read_csv(path, header=None)[0]
    hours = pd.to_datetime(s, utc=True).dt.floor("H")
    return pd.DatetimeIndex(hours)
