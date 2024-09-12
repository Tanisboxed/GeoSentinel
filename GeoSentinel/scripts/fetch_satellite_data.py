import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import psycopg2

load_dotenv()

PLANET_API_KEY= os.getenv('PLANET_API_KEY')
DB_URL = os.getenv('DATABASE_URL')

def fetch_satellite_data(start_data, end_data, aoi):
    