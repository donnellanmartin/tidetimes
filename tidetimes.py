import requests
from datetime import datetime

# Define the API URL for WorldTides data
API_URL = "https://www.worldtides.info/api/v2"

# Parameters for Carraroe, Ireland with your WorldTides API key
PARAMS = {
    'lat': '53.299',  # Latitude for Carraroe
    'lon': '-9.553',  # Longitude for Carraroe
    'timezone': 'GMT',
    'datum': 'MLLW',  # Mean Lower Low Water (optional parameter)
    'key': 'your_api_key_here'  # Replace with your WorldTides API key
}

def get_tide_data():
    response = requests.get(API_URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        return data.get('extremes', [])
    else:
        print("Error fetching data:", response.status_code)
        return []

def display_tide_times(tides):
    print("Tide Times for Carraroe:")
    for tide in tides:
        tide_time = datetime.fromtimestamp(tide['dt']).strftime('%Y-%m-%d %H:%M:%S')
        height = tide['height']
        print(f"Time: {tide_time}, Height: {height} m")

def main():
    tides = get_tide_data()
    if tides:
        display_tide_times(tides)

if __name__ == "__main__":
    main()
