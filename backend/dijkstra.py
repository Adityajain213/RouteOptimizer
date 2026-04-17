import heapq

def dijkstra_route(distance_matrix):
    n = len(distance_matrix)
    graph = {i: {} for i in range(n)}

    # Build the adjacency list (Graph + HashMap)
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = distance_matrix[i][j]

    # Dijkstra with priority queue (Heap)
    start = 0
    visited = set()
    distances = [float('inf')] * n
    previous = [None] * n
    distances[start] = 0

    heap = [(0, start)]  # (distance, node)

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    heapq.heappush(heap, (new_dist, neighbor))

    # Build the optimized path (backtrack using Stack)
    path = [start]
    current = start 
    while len(path) < n:
        next_node = None
        min_dist = float('inf')
        for neighbor in range(n):
            if neighbor not in path and distance_matrix[current][neighbor] < min_dist:
                min_dist = distance_matrix[current][neighbor]
                next_node = neighbor
        if next_node is not None:
            path.append(next_node)
            current = next_node
        else:
            break

    return path
