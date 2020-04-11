class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        max_profit = 0

        for current_time in len(1, prices):
            if prices[current_time + 1] > prices[current_time]:
                max_profit += prices[current_time + 1] - prices[current_time]
        return max_profit
