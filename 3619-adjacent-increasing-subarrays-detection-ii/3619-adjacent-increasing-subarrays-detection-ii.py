class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        pre = 0
        cur = 0
        ans = 0
        
        for i in range(n):
            cur += 1
            
            if i == n - 1 or nums[i] >= nums[i + 1]:
                ans = max(ans, cur // 2, min(pre, cur))
                
                pre = cur
                cur = 0
        
        return ans
