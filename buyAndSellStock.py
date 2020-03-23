class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return None
        

        minimum_price = prices[0]
        max_profit = prices[1] - minimum_price

        for current_time in prices:
            current_price = prices[current_time]

            potential_profit = current_price - minimum_price
            max_profit = max(potential_profit, max_profit)
            minimum_price = min(minimum_price, current_price)
        return max_profit

        