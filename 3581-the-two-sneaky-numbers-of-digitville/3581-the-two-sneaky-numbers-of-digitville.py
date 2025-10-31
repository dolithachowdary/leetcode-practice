from typing import List
from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [x for x, c in freq.items() if c == 2]
