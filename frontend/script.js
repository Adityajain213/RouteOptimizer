
let map = L.map('map').setView([18.5204, 73.8567], 11);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);


setTimeout(() => {
  map.invalidateSize();
}, 300);


const warehouse = [18.5204, 73.8567];


const warehouseMarker = L.circleMarker(warehouse, {
  radius: 8,
  color: 'red',
  fillColor: 'red',
  fillOpacity: 0.9
}).addTo(map).bindPopup("🏢 Warehouse");


document.getElementById('csvFile').addEventListener('change', handleCSVUpload);

function handleCSVUpload(e) {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (event) => {
    const lines = event.target.result.trim().split("\n");
    const locations = lines.map((line) => {
      const [lat, lng] = line.split(',').map(parseFloat);
      return { lat, lng };
    });

    showTable(locations);
    sendToBackend(locations);
  };
  reader.readAsText(file);
}


function showTable(locations) {
  const table = document.getElementById('locationTable');
  table.innerHTML = "<tr><th>#</th><th>Latitude</th><th>Longitude</th></tr>";
  locations.forEach((loc, i) => {
    table.innerHTML += `<tr><td>${i + 1}</td><td>${loc.lat}</td><td>${loc.lng}</td></tr>`;
  });
}


function sendToBackend(locations) {
  fetch('http://127.0.0.1:5000/optimize-route', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ locations })
  })
    .then(res => {
      if (!res.ok) throw new Error('Failed to fetch route');
      return res.json();
    })
    .then(data => {
      plotRoute(data.route, data.geojson);  
      showSummary(data.summary);
    })
    .catch(err => {
      console.error("API Error:", err);
      alert("Route optimization failed. Check console for details.");
    });
}


let routePolyline = null;
let routeMarkers = [];

function plotRoute(route, geojson) {

  if (routePolyline) map.removeLayer(routePolyline);
  routeMarkers.forEach(m => map.removeLayer(m));
  routeMarkers = [];

  routePolyline = L.geoJSON(geojson, {
    style: { color: 'lime', weight: 4 }
  }).addTo(map);

  // Add markers (red for warehouse, blue for stops)
  route.forEach((pt, i) => {
    const marker = L.circleMarker([pt.lat, pt.lng], {
      radius: 6,
      color: i === 0 ? 'red' : 'blue',
      fillColor: i === 0 ? 'red' : 'blue',
      fillOpacity: 0.9
    })
      .addTo(map)
      .bindPopup(i === 0 ? "Warehouse" : `Point ${i}`);
    routeMarkers.push(marker);
  });

  
  map.fitBounds(routePolyline.getBounds(), { padding: [30, 30] });
}

function showSummary(summary) {
  const table = document.getElementById('summaryTable');
  table.innerHTML = "<tr><th>From</th><th>To</th><th>Distance (km)</th></tr>";

  summary.forEach(s => {
    if (s.total_distance_km !== undefined) {
      table.innerHTML += `
        <tr><td colspan="2"><strong>Total Distance</strong></td>
        <td><strong>${s.total_distance_km.toFixed(2)}</strong></td></tr>`;
    } else {
      table.innerHTML += `<tr><td>${s.from}</td><td>${s.to}</td><td>${s.distance_km.toFixed(2)}</td></tr>`;
    }
  });
}
