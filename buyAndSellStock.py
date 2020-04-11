class Solution:
    def maxProfit(self, prices: List[int]) -> int:
<<<<<<< HEAD
        

        max_profit = 0

        for current_time in len(1, prices):
            if prices[current_time + 1] > prices[current_time]:
                max_profit += prices[current_time + 1] - prices[current_time]
        return max_profit
=======
        max_profit = 0
        if len(prices) == 0 or len(prices) < 2:
            return False

        for current_time in len(prices) - 1:
<<<<<<< HEAD
            if prices[current_time + 1] > prices[current_time]:
                max_profit += prices[current_time + 1] - prices[current_time]
        return max_profit
        
=======
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
>>>>>>> bb0b42944939cdc72b297f1370fb7e86c922684e
>>>>>>> 42daa26ba319d771cf92b792ac11fa76c1fe20b5
