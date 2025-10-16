class Solution:
    def findSmallestInteger(self, nums, value):
        freq = {}

        # Step 1: compute remainder frequencies
        for num in nums:
            r = (num % value + value) % value  # handle negative numbers
            if r in freq:
                freq[r] += 1
            else:
                freq[r] = 1

        # Step 2: find smallest missing integer
        x = 0
        while True:
            r = x % value
            if r not in freq or freq[r] == 0:
                return x
            freq[r] -= 1
            x += 1
