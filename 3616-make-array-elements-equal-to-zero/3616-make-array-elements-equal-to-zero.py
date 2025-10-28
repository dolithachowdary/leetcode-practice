class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        ans = 0

        for x in nums:
            if x == 0:
                if 2 * left == total:
                    ans += 2           # either direction works
                elif abs(2 * left - total) == 1:
                    ans += 1           # only the side with larger sum works
            left += x

        return ans
