import requests
import pandas as pd
import os


LAT = 24.8949
LON = 91.8687
START_DATE = "20150101" 
END_DATE = "20241231"   

def fetch_sylhet_solar_data():
    print(f"--- Initiating Data Fetch for Sylhet ({LAT}, {LON}) ---")
    
    
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point?"
        f"parameters=ALLSKY_SFC_SW_DWN,T2M,RH2M&"
        f"community=RE&longitude={LON}&latitude={LAT}&"
        f"start={START_DATE}&end={END_DATE}&format=JSON"
    )
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status() 
        data = response.json()
        
       
        features = data['properties']['parameter']
        df = pd.DataFrame(features)
        
        
        output_path = "data/raw/sylhet_solar_raw.csv"
        df.to_csv(output_path)
        
        print(f"SUCCESS: Dataset saved to {output_path}")
        print(f"Total Days Captured: {len(df)}")
        
    except Exception as e:
        print(f"FAILURE: Research interrupted by error: {e}")

if __name__ == "__main__":
    fetch_sylhet_solar_data()
