"""
Physics-Informed ML for Solar Microgrid Resilience — Sylhet
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Script: download_nasa_power.py
Author: Prosun Datta

Description:
    Downloads 20 years of hourly weather data for Sylhet,
    Bangladesh from the NASA POWER API and saves it to
    data/raw/sylhet_nasa_power.csv.

    Location: 24.89°N, 91.87°E (Sylhet)
    Period:   2005-01-01 to 2024-12-31
    Resolution: hourly

Usage:
    python scripts/download_nasa_power.py
"""

import requests
import pandas as pd
import os

# ── Configuration ─────────────────────────────────────────────────
LAT        = 24.89
LON        = 91.87
START_DATE = "20050101"
END_DATE   = "20241231"
PARAMETERS = "ALLSKY_SFC_SW_DWN,CLRSKY_SFC_SW_DWN,T2M,RH2M,PRECTOTCORR,WS10M"
OUTPUT_PATH = "data/raw/sylhet_nasa_power.csv"

NASA_POWER_URL = (
    f"https://power.larc.nasa.gov/api/temporal/hourly/point"
    f"?parameters={PARAMETERS}"
    f"&community=RE"
    f"&longitude={LON}"
    f"&latitude={LAT}"
    f"&start={START_DATE}"
    f"&end={END_DATE}"
    f"&format=CSV"
)


def download():
    """Download NASA POWER data and save to CSV."""
    print(f"Downloading NASA POWER data for Sylhet ({LAT}N, {LON}E)...")
    print(f"Period: {START_DATE} to {END_DATE}")
    print(f"Parameters: {PARAMETERS}")
    print("This may take a few minutes...")

    # TODO: implement API call and save
    # response = requests.get(NASA_POWER_URL, timeout=120)
    # response.raise_for_status()
    # with open(OUTPUT_PATH, 'w') as f:
    #     f.write(response.text)
    # print(f"Saved to {OUTPUT_PATH}")
    pass


if __name__ == '__main__':
    os.makedirs("data/raw", exist_ok=True)
    download()
