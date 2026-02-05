class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        for index, value in enumerate(nums):
            if value > 0:
                res.append(nums[(index+value) % length])
            elif value < 0:
                res.append(nums[(index - abs(value) + length) % length])
            else:
                res.append(0)
        return res