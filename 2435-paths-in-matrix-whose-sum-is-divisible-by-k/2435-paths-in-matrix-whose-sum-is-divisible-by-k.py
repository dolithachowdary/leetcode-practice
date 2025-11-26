class Solution:
    MOD = 10**9 + 7

    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] will be an array length k of counts for remainders at cell (i,j)
        dp = [[[0]*k for _ in range(n)] for __ in range(m)]

        start_r = grid[0][0] % k
        dp[0][0][start_r] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cell = grid[i][j]
                cur = dp[i][j]
                # from top
                if i > 0:
                    top = dp[i-1][j]
                    for r in range(k):
                        if top[r]:
                            new_r = (r + cell) % k
                            cur[new_r] = (cur[new_r] + top[r]) % self.MOD
                # from left
                if j > 0:
                    left = dp[i][j-1]
                    for r in range(k):
                        if left[r]:
                            new_r = (r + cell) % k
                            cur[new_r] = (cur[new_r] + left[r]) % self.MOD

        return dp[m-1][n-1][0] % self.MOD
