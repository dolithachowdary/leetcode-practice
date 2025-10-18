class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        occupied = float('-inf')
        ans = 0
        
        for x in nums:
            low = x - k
            high = x + k
            # we want to assign cur = max(occupied + 1, low)
            cur = max(occupied + 1, low)
            if cur <= high:
                # we can assign a new distinct value
                ans += 1
                occupied = cur
            # else: we skip (can't assign a new distinct value in that range)
        
        return ans
