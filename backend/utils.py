import openrouteservice


ORS_API_KEY = "5b3ce3597851110001cf624892a30fa5bd1a46b4b94fc8e3d1620b12" 

client = openrouteservice.Client(key=ORS_API_KEY)

def get_road_distance_matrix(locations):
    coordinates = [(loc["lng"], loc["lat"]) for loc in locations]
    response = client.distance_matrix(
        locations=coordinates,
        profile='driving-car',
        metrics=['distance'],
        units='km'
    )
    return response['distances']

def get_route_polyline(locations, route_indices):
    coordinates = [(locations[i]['lng'], locations[i]['lat']) for i in route_indices]
    response = client.directions(
        coordinates=coordinates,
        profile='driving-car',
        format='geojson'
    )
    return response['features'][0]['geometry']

def format_route_summary(locations, matrix, route_indices):
    summary = []
    total = 0
    for i in range(len(route_indices) - 1):
        from_idx = route_indices[i]
        to_idx = route_indices[i + 1]
        dist = round(matrix[from_idx][to_idx], 2)
        total += dist
        summary.append({
            "from": "Warehouse" if i == 0 else f"Point {i}",
            "to": f"Point {i+1}",
            "distance_km": dist
        })
    summary.append({"total_distance_km": round(total, 2)})
    return summary
