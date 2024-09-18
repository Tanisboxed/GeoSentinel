import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import psycopg2

load_dotenv()

ACLED_API_KEY = os.getenv('ACLED_API_KEY')
DB_URL = os.getenv('DATABASE_URL')

def fetch_conflict_data(start_date, end_date):
    base_url = "https://api.acleddata.com/acled/read"
    
    params = {
        "key": ACLED_API_KEY,
        "email": os.getenv('ACLED_EMAIL'),
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "data_format": "json"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def store_conflict_data(data):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    for item in data:
        event_id = item['data_id']
        event_date = item['event_date']
        event_type = item['event_type']
        actor1 = item['actor1']
        actor2 = item['actor2']
        location = item['location']
        latitude = item['latitude']
        longitude = item['longitude']
        notes = item['notes']
        cur.execute("""
            INSERT INTO conflict_data (event_id, event_date, event_type, actor1, actor2, location, latitude, longitude, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (event_id) DO UPDATE
            SET event_date = EXCLUDED.event_date,
                event_type = EXCLUDED.event_type,
                actor1 = EXCLUDED.actor1,
                actor2 = EXCLUDED.actor2,
                location = EXCLUDED.location,
                latitude = EXCLUDED.latitude,
                longitude = EXCLUDED.longitude,
                notes = EXCLUDED.notes
        """, (event_id, event_date, event_type, actor1, actor2, location, latitude, longitude, notes))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    conflict_data = fetch_conflict_data(start_date, end_date)
    if conflict_data:
        store_conflict_data(conflict_data)
        print(f"Stored {len(conflict_data)} conflict data items.")
    else:
        print("No conflict data fetched.")
