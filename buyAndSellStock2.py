class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if price is None or len(prices) == 0:
            return None
        profit = 0
        for price in range(len(prices)):
            if prices[price + 1] > prices[price]:
                profit += prices[price + 1] - prices[price]
        return profit 
