class Solution:
    def minDeletionSize(self, strs):
        rows = len(strs)
        cols = len(strs[0])

        dp = [1] * cols

        for j in range(cols):
            for i in range(j):
                ok = True
                for r in range(rows):
                    if strs[r][i] > strs[r][j]:
                        ok = False
                        break
                if ok:
                    dp[j] = max(dp[j], dp[i] + 1)

        return cols - max(dp)
