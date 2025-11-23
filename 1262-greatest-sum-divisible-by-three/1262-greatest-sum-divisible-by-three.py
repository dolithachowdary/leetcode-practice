class Solution:
    def maxSumDivThree(self, nums):
        r1, r2 = [], []
        total = sum(nums)

        for n in nums:
            if n % 3 == 1:
                r1.append(n)
            elif n % 3 == 2:
                r2.append(n)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            remove1 = r1[0] if len(r1) >= 1 else float('inf')
            remove2 = r2[0] + r2[1] if len(r2) >= 2 else float('inf')
            return total - min(remove1, remove2)

        if total % 3 == 2:
            remove1 = r2[0] if len(r2) >= 1 else float('inf')
            remove2 = r1[0] + r1[1] if len(r1) >= 2 else float('inf')
            return total - min(remove1, remove2)
