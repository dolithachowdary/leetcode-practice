class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_distances(start):
            dist = [-1] * n
            d = 0
            while start != -1 and dist[start] == -1:
                dist[start] = d
                start = edges[start]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        ans = -1
        best = float('inf')

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                maxd = max(dist1[i], dist2[i])
                if maxd < best:
                    best = maxd
                    ans = i

        return ans
