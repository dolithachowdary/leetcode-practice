class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        def count(arr):
            hm = {}
            for i in arr:
                if i in hm:
                    hm[i]+=1
                else:
                    hm[i] = 1
            return hm

        for i in range(len(nums)-k+1):
            hm = count(nums[i:i+k])
            sorted_items = sorted(hm.items(), key=lambda p: (-p[1], -p[0]))

            total = 0
            for num,freq in sorted_items[:x]:
                total += num*freq
            res.append(total)
        return res