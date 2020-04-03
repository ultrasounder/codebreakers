class Solution:
    def rob(self, nums: List[int]) -> int:
#A new solution that I came up with PR
    #attack the base cases first like recursion
    if nums is None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp = [0] * len(nums)#Initalize a DP array for the size of the length of nums array
    dp[0] = nums[0]# the amount we can get by robbing 2 houses
    dp[1] = max(nums[0], nums[1]) # for two houses, well max of the first and second house
    for in range(2, len(dp)): # now for the nth house, our recurrence is current house and two houses before or the previous house
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    return dp[n-1]