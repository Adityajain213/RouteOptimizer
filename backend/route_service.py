import requests

ORS_API_KEY = "YOUR API KEY"  # Replace this with your free ORS key

def get_route(coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": coords,
        "format": "geojson"
    }

    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("ORS Error:", response.text)
        return None
