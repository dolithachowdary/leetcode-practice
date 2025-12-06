from collections import deque

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # dp[i] = #ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1

        # pref[i] = dp[0] + ... + dp[i]
        pref = [0] * (n + 1)
        pref[0] = 1

        maxq = deque()  # decreasing (store indices)
        minq = deque()  # increasing (store indices)

        L = 0  # left boundary of valid window

        for r in range(n):  # r is 0-based index in nums
            # maintain max deque
            while maxq and nums[r] > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(r)

            # maintain min deque
            while minq and nums[r] < nums[minq[-1]]:
                minq.pop()
            minq.append(r)

            # shrink window until it becomes valid
            while nums[maxq[0]] - nums[minq[0]] > k:
                if maxq[0] == L:
                    maxq.popleft()
                if minq[0] == L:
                    minq.popleft()
                L += 1

            # valid starting j are L..r; they correspond to dp[L]..dp[r]
            if L == 0:
                ways = pref[r]
            else:
                ways = (pref[r] - pref[L - 1]) % MOD

            dp[r + 1] = ways
            pref[r + 1] = (pref[r] + dp[r + 1]) % MOD

        return dp[n]
