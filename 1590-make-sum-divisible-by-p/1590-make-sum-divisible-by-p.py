from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0
        
        pref = 0
        best = n  # initialize as impossible large (can't remove whole array)
        last_index = {0: -1}  # prefix modulo -> last index (prefix before start has index -1)
        
        for i, val in enumerate(nums):
            pref = (pref + val) % p
            # we need previous prefix `prev` such that (pref - prev) % p == r
            target = (pref - r) % p
            if target in last_index:
                length = i - last_index[target]
                if length < best:
                    best = length
            # update last seen index for this prefix modulo
            last_index[pref] = i
        
        return best if best < n else -1
