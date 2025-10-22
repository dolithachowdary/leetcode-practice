from collections import Counter

class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        line = {}            # difference map: key -> delta
        candidates = set()   # possible T values to check
        
        for x in nums:
            start = x - k
            endp1 = x + k + 1
            line[start] = line.get(start, 0) + 1
            line[endp1] = line.get(endp1, 0) - 1
            candidates.add(x)
            candidates.add(start)
            candidates.add(endp1)
        
        ans = 1
        adjustable = 0
        
        for T in sorted(candidates):
            adjustable += line.get(T, 0)
            already = cnt.get(T, 0)
            canChange = adjustable - already
            freqHere = already + min(numOperations, canChange)
            ans = max(ans, freqHere)
        
        return ans
