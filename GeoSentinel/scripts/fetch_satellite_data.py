import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import psycopg2

load_dotenv()

PLANET_API_KEY = os.getenv('PLANET_API_KEY')
DB_URL = os.getenv('DATABASE_URL')

def fetch_satellite_data(start_date, end_date, aoi):
    base_url = "https://api.planet.com/data/v1"
    search_url = f"{base_url}/quick-search"
    search_request = {
        "item_types": ["PSScene"],
        "filter": {
            "type": "AndFilter",
            "config": [
                {
                    "type": "DateRangeFilter",
                    "field_name": "acquired",
                    "config": {
                        "gte": start_date.isoformat(),
                        "lte": end_date.isoformat()
                    }
                },
                {
                    "type": "GeometryFilter",
                    "field_name": "geometry",
                    "config": aoi
                }
            ]
        }
    }
    headers = {"Authorization": f"Basic {PLANET_API_KEY}"}
    response = requests.post(search_url, json=search_request, headers=headers)
    
    if response.status_code == 200:
        results = response.json()
        return results['features']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def store_satellite_data(data):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    for item in data:
        id = item['id']
        acquired = item['properties']['acquired']
        cloud_cover = item['properties']['cloud_cover']
        geometry = item['geometry']
        cur.execute("""
            INSERT INTO satellite_data (id, acquired, cloud_cover, geometry)
            VALUES (%s, %s, %s, ST_GeomFromGeoJSON(%s))
            ON CONFLICT (id) DO UPDATE
            SET acquired = EXCLUDED.acquired,
                cloud_cover = EXCLUDED.cloud_cover,
                geometry = EXCLUDED.geometry
        """, (id, acquired, cloud_cover, json.dumps(geometry)))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()
    aoi = {
        "type": "Polygon",
        "coordinates": [
            [
                [-122.54, 37.81],
                [-122.54, 37.46],
                [-122.35, 37.46],
                [-122.35, 37.81],
                [-122.54, 37.81]
            ]
        ]
    }

    satellite_data = fetch_satellite_data(start_date, end_date, aoi)
    if satellite_data:
        store_satellite_data(satellite_data)
        print(f"Stored {len(satellite_data)} satellite data items.")
    else:
        print("No satellite data fetched.")
