class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        from collections import Counter
        cnt = Counter(nums)
        line = {}
        candidates = set()
        
        for x in nums:
            # mark range [x-k, x+k]
            start = x - k
            endp1 = x + k + 1
            line[start] = line.get(start, 0) + 1
            line[endp1] = line.get(endp1, 0) - 1
            # add candidate values
            candidates.add(x)
            candidates.add(start)
            candidates.add(endp1)
        
        ans = 1
        adjustable = 0
        for v in sorted(candidates):
            adjustable += line.get(v, 0)
            already = cnt.get(v, 0)
            non_equal = adjustable - already
            # we can convert at most numOperations of the non_equal ones
            ans = max(ans, already + min(numOperations, non_equal))
        
        return ans