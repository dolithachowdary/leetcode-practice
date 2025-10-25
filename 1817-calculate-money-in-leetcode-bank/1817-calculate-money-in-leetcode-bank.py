class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        
        # total for complete weeks
        total = 7 * weeks * (weeks + 1) // 2 + 21 * weeks
        
        # total for remaining days in next week
        total += days * (2 * weeks + days + 1) // 2
        
        return total
