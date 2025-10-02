class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1  
            total += 1
            empty += 1  

        return total
