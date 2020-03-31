class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0 or len(prices) < 2:
            return False

        for current_time in len(prices) - 1:
            if prices[current_time + 1] > prices[current_time] 
            
'''
This looks like it isn't quite finished yet. I would approach the problem doing something like this:

def maxProfit(prices: List[int]) -> int:
        smallest = float('inf')
        curMax = 0
        for price in prices:
            smallest = min(smallest, price)
            curMax = max(curMax, price-smallest)
        return curMax
        
Once you get the rest of the code pushed, let me know and I can review it again!
'''
