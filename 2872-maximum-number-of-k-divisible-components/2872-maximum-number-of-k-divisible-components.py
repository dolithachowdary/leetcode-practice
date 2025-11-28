class Solution:
    def maxKDivisibleComponents(self, n, edges, values, k):
        from collections import defaultdict
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = [False] * n
        self.comp = 0

        def dfs(u):
            visited[u] = True
            subtotal = values[u] % k

            for v in g[u]:
                if not visited[v]:
                    child_mod = dfs(v)

                    if child_mod == 0:
                        # Child forms a separate component
                        self.comp += 1
                    else:
                        subtotal = (subtotal + child_mod) % k

            return subtotal

        root_mod = dfs(0)

        # If root subtree also divisible by k → counts as one component
        # If root_mod == 0: self.comp already includes it since it's the last remaining part.
        return self.comp + (1 if root_mod == 0 else 0)
