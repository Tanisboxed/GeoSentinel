# import requests
# import pandas as pd

# EMAIL = 'adithya.pillai16@gmail.com'
# API_KEY = 'K39bxYHnd8qXAokqJblY'
# ACLED_URL = 'https://api.acleddata.com/acled/read'  # Use ACLED's API endpoint for dataset

# def fetch_acled_data(start_date="2023-01-01",end_date="2023-12-31", country=None, limit=100000):
#     headers={
#         'Accept':'application/json',
#         'Content-Type':'application/json'
#     }
#     params = {
#         'email': EMAIL,
#         'key': API_KEY,
#         'country': 'any',  # Specify country if needed
#         'start_date': start_date,
#         'end_date':end_date,
#         'format': 'json',
#         'limit': limit
#     }
#     try:
#         response =requests.get(ACLED_URL,headers=headers,params=params)
#         response.raise_for_status()
#         data =response.json().get('data',[])
#         print("Data fetched successfully.")
#         print(f"Data: {data}")
#         return pd.DataFrame(data)
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return pd.DataFrame()

# if __name__ == "__main__":
#     df = fetch_acled_data(start_date="2023-01-01",end_date="2023-12-31", country=None)
#     if not df.empty:
#         df.to_csv("data/acled_data.csv", index=False)
#         print("Data saved to acled_data.csv")
#     else:
#         print("No data returned")



import requests
import pandas as pd
from io import StringIO

EMAIL = 'adithya.pillai16@gmail.com'
API_KEY = 'K39bxYHnd8qXAokqJblY'
ACLED_URL = 'https://api.acleddata.com/acled/read.csv'

def fetch_acled_data(start_date="2022-01-01", end_date="2022-12-31", country=None, limit=100000):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    params = {
        'email': EMAIL,
        'key': API_KEY,
        'country': country if country else 'any',  # Specify country if needed
        'event_date': f'{start_date}|{end_date}',  # Correct date range format
        'event_date_where': 'BETWEEN',
        'format': 'json',  # Response format is JSON metadata
        'limit': limit
    }
    
    try:
        response = requests.get(ACLED_URL, headers=headers, params=params)
        response.raise_for_status()
        
        # Print the raw response content for debugging
        print("Raw Response Content:")
        print(response.text[:500])  # Print first 500 characters
        
        # Check for error messages in the response
        if "Error" in response.text:
            print(f"API Error: {response.text}")
            return pd.DataFrame()
        
        # Check if the response is in CSV format
        if response.headers['Content-Type'].startswith('text/csv'):
            # Check if the response has content
            if response.text.strip():
                # Read CSV content into a DataFrame
                df = pd.read_csv(StringIO(response.text))
                print("Data fetched successfully.")
                return df
            else:
                print("Error: Empty CSV response.")
                return pd.DataFrame()
        else:
            print("Error: Response is not in CSV format.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_acled_data(start_date="2022-01-01", end_date="2022-12-31", country='Georgia')  # Adjusted the date range
    if not df.empty:
        df.to_csv("data/acled_data.csv", index=False)
        print("Data saved to acled_data.csv")
    else:
        print("No data returned")
