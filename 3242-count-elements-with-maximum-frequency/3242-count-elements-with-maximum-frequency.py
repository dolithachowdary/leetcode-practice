class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = {}
        
        # Count frequency of each number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Find maximum frequency
        maxFreq = 0
        for val in freq.values():
            if val > maxFreq:
                maxFreq = val
        
        # Count total occurrences of numbers with max frequency
        result = 0
        for val in freq.values():
            if val == maxFreq:
                result += val
        
        return result
