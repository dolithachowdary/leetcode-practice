class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        r = total % k
        return r   # minimum operations needed
