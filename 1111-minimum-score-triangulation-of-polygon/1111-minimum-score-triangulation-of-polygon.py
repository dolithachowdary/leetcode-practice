class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        # gap = length of interval
        for gap in range(2, n):  # at least 3 vertices
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = float("inf")
                for k in range(i+1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    )
        
        return dp[0][n-1]
