class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)

        maxSubArraySum = float('inf')

        left = 0 # Left Array Bound
        # right = left

        # for left in range(n):
        #     for right in range(n):
        #         windowSum = 0
        #         k = left

        #         for k in range(right):
        #             windowSum += nums[k]
        #         maxSubArraySum = max(maxSubArraySum, windowSum)
        # return maxSubArraySum

        # for left in range(n):
        #     runningWindowSum = 0
        #     for right in range(left, n):
        #         runningWindowSum += nums[right]
        #         maximumSubArraySum = abs(maxSubArraySum, runningWindowSum)

        # return maximumSubArraySum

        #We default to say that the best element is the first element
        #we also default to say that the best max ending element is the first element
        maxSoFar = 0
        maxEndingHere = nums[0]
        #we will investigate the rest of the items in the array from index 1 onward
        for in range(1, n):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])

            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar