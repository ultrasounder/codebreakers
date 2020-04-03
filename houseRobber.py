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

'''
A few comments looking through this:
1. We want to make sure we indent our code both for readability and running (Python) purposes (lines 5-16)
2. We want to make sure we have i defined in our for loop (line 14)
3. We want to make sure n is defined (line 16)

Otherwise, your solution is even more concise than what we talked about in our lesson. I typically do not teach it that way because I
find it much easier to wrap my head around the other way when doing it for the first time. This is a great solution. My solution is 
similiar. We can be more concise in the base case checks, etc. but the idea is exactly the same. For the base cases, we know that if
the length of the array is less than 3, we just rob the max house, so we can collapse our edge cases down a bit. Besides that, everything
looks really good. Nice work!

class Solution:
    def rob(self, arr):
        if not arr: return 0
        if len(arr) < 3: return max(arr)
        dp = [0] * len(arr)
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])
        for i in range(2, len(arr)):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])
        return dp[-1]
'''
