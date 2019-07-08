class Solution:
    def maxProfit(self, prices) -> int:
        maxVal = 0
        current = float("inf")
        for price in prices:
            if price < current:
                current = price
            else:
                maxVal = max(maxVal, price-current)

        return maxVal