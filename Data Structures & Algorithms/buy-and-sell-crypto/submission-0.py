class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                maxProf = max(maxProf, profit)
        return maxProf
