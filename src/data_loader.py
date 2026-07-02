"""
QX-01: Physics-Informed ML for Solar Microgrid Resilience — Sylhet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module: data_loader.py
Author: Prosun Datta
Organisation: QYSICA
Contact: prosunkdatta@gmail.com

Description:
    Loads and cleans 20 years of hourly NASA POWER satellite data
    for Sylhet, Bangladesh (24.89°N, 91.87°E). Produces a clean
    DataFrame ready for feature engineering.

Input:
    data/raw/sylhet_nasa_power.csv — raw NASA POWER download

Output:
    pandas.DataFrame — cleaned, datetime-indexed hourly weather data

Usage:
    from src.data_loader import load_nasa_power, clean_nasa
    df = load_nasa_power('data/raw/sylhet_nasa_power.csv')
"""

import pandas as pd
import numpy as np


# ── Column name mapping from NASA POWER API ──────────────────────
NASA_COLUMN_MAP = {
    'ALLSKY_SFC_SW_DWN': 'GHI',
    'CLRSKY_SFC_SW_DWN': 'CLRSKY',
    'T2M':               'T2M',
    'RH2M':              'RH2M',
    'PRECTOTCORR':       'PRECIP',
    'WS10M':             'WS10M',
}

# NASA POWER fill value (represents missing data)
NASA_FILL_VALUE = -999.0


def load_nasa_power(filepath: str) -> pd.DataFrame:
    """
    Load raw NASA POWER CSV file into a clean pandas DataFrame.

    Parameters
    ----------
    filepath : str
        Path to the raw NASA POWER CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with datetime index and renamed columns.
        Rows with missing values are removed.
    """
    # TODO: implement after confirming NASA POWER CSV column names
    # from the actual downloaded file
    pass


def clean_nasa(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a raw NASA POWER DataFrame.

    Steps:
        1. Replace NASA fill values (-999) with NaN
        2. Drop rows with any NaN values
        3. Clip GHI and CLRSKY to non-negative values
        4. Ensure datetime index is sorted

    Parameters
    ----------
    df : pd.DataFrame
        Raw NASA POWER DataFrame with datetime index.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame ready for feature engineering.
    """
    # TODO: implement
    pass


def validate_data(df: pd.DataFrame) -> dict:
    """
    Validate the cleaned DataFrame and return a summary report.

    Checks:
        - Expected number of rows (~175,200 for 20 years hourly)
        - No remaining NaN values
        - GHI values in valid range [0, 1400] W/m²
        - Date range covers 2005-2024

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned DataFrame.

    Returns
    -------
    dict
        Validation report with pass/fail for each check.
    """
    # TODO: implement
    pass


if __name__ == '__main__':
    df = load_nasa_power('data/raw/sylhet_nasa_power.csv')
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Date range: {df.index.min()} to {df.index.max()}")
    print(df.head())
