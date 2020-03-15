'''746. Min Cost Climbing Stairs'''
'''On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]* (len(cost) + 1) #initialize dp array
        if len(cost) < 2:
            return cost[1]
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(len(cost) + 1):
            dp[i] = min(dp[i-1], dp[i-2]) + (0 if i == len(cost) else cost[i])
        return dp[-1]