# Route Optimizer

## Overview
This project is a route optimization system that finds an efficient path across multiple locations.  
I built it to understand how navigation and delivery systems work behind the scenes using graph algorithms and real-world distance data.

---

## What it does
- Takes multiple locations as input  
- Fetches real distance data using OpenRouteService  
- Computes an optimized route  
- Returns ordered path with total distance  

---

## Tech Stack
- **Frontend:** React / HTML-CSS-JS  
- **Backend:** Node.js / Flask  
- **API:** OpenRouteService  
- **Algorithms:** Dijkstra, Nearest Neighbor  

---

## Project Structure

route-optimizer/
├── frontend/ # UI
├── backend/ # server + logic
│ ├── routes/
│ ├── services/
│ └── utils/
└── README.md


---

## OpenRouteService API Setup
1. Go to https://openrouteservice.org/  
2. Sign up and log in  
3. Open Dashboard → API Keys  
4. Generate a key  

Create a `.env` file in backend:


OPENROUTESERVICE_API_KEY=your_api_key
Run Locally
Backend
cd backend
npm install
npm start
Frontend
cd frontend
npm install
npm start
How it works

Locations are converted into coordinates and used to build a graph.

Dijkstra is used for shortest paths
A greedy approach is used to order multiple stops

It’s not a perfect solution (like exact TSP), but it’s fast and works well for practical cases.


Limitations
Uses approximation for multi-stop routing
Depends on external API response time
No real-time traffic
Why I built this

I wanted to go beyond just learning Dijkstra and actually use it in something practical.
This helped me understand how routing problems are handled in real systems.


---

### What changed (important)
- Proper headings (`##`)  
- Spacing between sections  
- Code blocks formatted correctly  
- Lists instead of long sentences  
- Clean structure → looks professional instantly  

---
