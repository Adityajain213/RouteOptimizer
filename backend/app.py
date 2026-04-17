from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_road_distance_matrix, get_route_polyline, format_route_summary
from dijkstra import dijkstra_route
from greedy_route import greedy_route
from dp_tsp import tsp_dp_route


app = Flask(__name__)
CORS(app)

WAREHOUSE = {"lat": 18.5204, "lng": 73.8567}  # Pune

@app.route('/optimize-route', methods=['POST'])
def optimize_route():
    data = request.get_json()
    locations = data.get("locations", [])
    if not locations:
        return jsonify({"error": "No locations provided"}), 400

    # 1. Add warehouse at the beginning
    all_points = [WAREHOUSE] + locations

    # 2. Get actual driving distance matrix from OpenRouteService
    try:
        distance_matrix = get_road_distance_matrix(all_points)
    except Exception as e:
        return jsonify({"error": "Failed to fetch road distances", "details": str(e)}), 500

    # 3. Decide algorithm
    if len(locations) <= 5:
        route = tsp_dp_route(distance_matrix)
    elif len(locations) <= 15:
        route = dijkstra_route(distance_matrix)
    else:
        route = greedy_route(distance_matrix)


    # 4. Prepare ordered points
    ordered_points = [all_points[i] for i in route]

    # 5. Get road polyline from OpenRouteService
    try:
        polyline_geojson = get_route_polyline(all_points, route)
    except Exception as e:
        return jsonify({"error": "Failed to fetch route polyline", "details": str(e)}), 500

    # 6. Get summary
    route_summary = format_route_summary(all_points, distance_matrix, route)

    return jsonify({
        "route": ordered_points,
        "summary": route_summary,
        "geojson": polyline_geojson
    })

if __name__ == '__main__':
    app.run(debug=True)
