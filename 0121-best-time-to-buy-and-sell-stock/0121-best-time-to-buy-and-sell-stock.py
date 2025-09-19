class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # update min price if current price is lower
            if price < min_price:
                min_price = price
            # check profit if we sell today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
