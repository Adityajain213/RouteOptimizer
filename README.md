#  Route Optimizer

A route optimization system that computes efficient paths across multiple locations using graph algorithms and real-world distance data.

---

## 🚀 Features

*  Accepts multiple locations (CSV or input)
*  Uses real-world or coordinate-based distance data
*  Computes optimized routes using multiple algorithms
*  Returns ordered path with total distance
*  Supports fast approximations and exact solutions

---

##  Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Algorithms:**

  * Dijkstra (Shortest Path)
  * Greedy (Nearest Neighbor)
  * Dynamic Programming (TSP)

---

## 📁 Project Structure

```bash
route-optimizer/
├── backend/
│   ├── app.py                # Main server (Flask)
│   ├── dijkstra.py          # Shortest path algorithm
│   ├── greedy_route.py      # Greedy route optimization
│   ├── dp_tsp.py            # Exact TSP (DP approach)
│   ├── route_service.py     # Core route logic
│   └── utils.py             # Helper functions
│
├── frontend/
│   ├── index.html           # UI
│   ├── script.js            # Client logic
│   └── styles.css           # Styling
│
├── test_big.csv             # Large dataset
├── test_coordinates.csv     # Sample coordinates
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔧 Backend (Python)

```bash
cd backend
pip install -r requirements.txt   # if requirements file exists
python app.py
```

### 🎨 Frontend

Open directly:

```bash
frontend/index.html
```

(or use Live Server in VS Code)

---

## 🧠 How It Works

* Input locations are converted into **coordinates**
* A graph is constructed using distance relationships
* Different algorithms are applied:

### 🔹 Dijkstra

* Finds shortest path between two nodes
* Efficient for single-source routing

### 🔹 Greedy (Nearest Neighbor)

* Selects closest next node
* Fast but approximate

### 🔹 Dynamic Programming (TSP)

* Computes optimal route across all nodes
* More accurate but computationally expensive

---

##  Key Highlights

* Implements **multiple routing strategies** in one system
* Demonstrates **trade-off between accuracy vs performance**
* Uses **real datasets (CSV inputs)**
* Modular backend design for extensibility

---

