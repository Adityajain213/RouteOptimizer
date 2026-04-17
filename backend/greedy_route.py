def greedy_route(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    path = [0]
    visited[0] = True

    for _ in range(n - 1):
        last = path[-1]
        min_dist = float('inf')
        next_node = -1
        for i in range(n):
            if not visited[i] and distance_matrix[last][i] < min_dist:
                min_dist = distance_matrix[last][i]
                next_node = i
        path.append(next_node)
        visited[next_node] = True

    return path
