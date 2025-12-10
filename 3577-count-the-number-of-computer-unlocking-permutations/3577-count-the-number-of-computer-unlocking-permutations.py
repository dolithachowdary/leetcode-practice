class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        import math

        MOD = 10**9 + 7


        N = len(complexity)
        # check if first computer is strictly less than all others
        for i in range(1, N):
            if complexity[0] >= complexity[i]:
                return 0
        return math.factorial(N-1) % MOD
