class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        if n>=3:
            return nums[n-3]
        else:
            return nums[n-1]

                
