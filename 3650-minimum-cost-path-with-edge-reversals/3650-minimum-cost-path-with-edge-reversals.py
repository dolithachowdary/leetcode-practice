import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        out = defaultdict(list)
        inc = defaultdict(list)

        for u, v, w in edges:
            out[u].append((v, w))
            inc[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0

        # Min-heap: (cost, node)
        pq = [(0, 0)]

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            if u == n - 1:
                return cost

            # Normal outgoing edges
            for v, w in out[u]:
                new_cost = cost + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

            # Reversed incoming edges (using switch)
            for v, w in inc[u]:
                new_cost = cost + 2 * w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        return -1
