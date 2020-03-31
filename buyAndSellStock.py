class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0 or len(prices) < 2:
            return False

        for current_time in len(prices) - 1:
            if prices[current_time + 1] > prices[current_time]:
                max_profit += prices[current_time + 1] - prices[current_time]
        return max_profit
        