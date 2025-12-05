class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total = sum(nums)
        n = len(nums)
        # If total sum is even, every split index 0..n-2 gives even |L-R|
        return n - 1 if total % 2 == 0 else 0
