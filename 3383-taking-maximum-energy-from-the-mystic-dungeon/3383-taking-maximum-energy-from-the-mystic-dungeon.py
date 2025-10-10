class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
            
        n = len(energy)
        dp = [0] * n

        # Compute from end to start
        for i in range(n - 1, -1, -1):
            jump = i + k
            if jump < n:
                dp[i] = energy[i] + dp[jump]
            else:
                dp[i] = energy[i]
        
        return max(dp)
