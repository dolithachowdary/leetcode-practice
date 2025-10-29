class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
       
        while (1 << k) - 1 < n:
            k += 1
        return (1 << k) - 1
