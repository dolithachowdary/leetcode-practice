class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert to list of integers
        arr = [int(ch) for ch in s]
        
        # Keep reducing until length = 2
        while len(arr) > 2:
            next_arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr)-1)]
            arr = next_arr
        
        # Now check if final two digits are equal
        return arr[0] == arr[1]
