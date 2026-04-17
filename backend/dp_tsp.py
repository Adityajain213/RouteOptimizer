# tsp_dp.py
from itertools import combinations

def tsp_dp_route(dist):
    n = len(dist)
    memo = {}
    
    for k in range(1, n):
        memo[(1 << k, k)] = (dist[0][k], 0)

    for r in range(2, n):
        for subset in combinations(range(1, n), r):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k:
                        continue
                    res.append((memo[(prev_bits, m)][0] + dist[m][k], m))
                memo[(bits, k)] = min(res)

    bits = (2 ** n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((memo[(bits, k)][0] + dist[k][0], k))
    opt, parent = min(res)

    # Reconstruct path
    path = [0]
    last = parent
    bits = (2 ** n - 1) - 1
    for i in range(n - 1):
        path.append(last)
        bits = bits & ~(1 << last)
        _, last = memo[(bits, last)]
    path.append(0)  # Return to start
    return path
