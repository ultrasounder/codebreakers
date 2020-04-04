class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastGoodIndexPosition = n - 1

        for i in range(n, -1):
            if i + nums[i] >= lastGoodIndexPosition:
                lastGoodIndexPosition = i
        return lastGoodIndexPosition
