import requests;
import pandas as pd; 
import io
import os
from dotenv import load_dotenv
load_dotenv()

def get_report_data():
    
    api_key= os.getenv("API_KEY")
    columns = [
            'day',
            'campaign_store_id', 'campaign_package_name', 'platform',
            'country', 'traffic_source',
            'campaign_id_external', 'campaign', 'campaign_type',
            'creative_set_id', 'creative_set',
            'ad_id', 'ad', 'ad_type', 'ad_creative_type',
            'cost', 'impressions', 'clicks', 'conversions', 'installs'
        ]
    params = {
            "api_key": api_key,
            "start": "2026-06-01",
            "end": "2026-06-07",
            "format": 'csv',
            "columns": ','.join(columns),
            'report_type': 'advertiser',
            'limit': 10,
        }
    url = "https://r.applovin.com/report"
    res = requests.get(url, params=params)
    try:
        res.raise_for_status()
        df = pd.read_csv(io.StringIO(res.text), dtype=str)
  
        df.to_csv("/opt/airflow/dags/report_from_applovin.csv", index=False, encoding='utf-8')
        

        print(df)
    except Exception as e:
        print(e)

