class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best_index = 0
        for i in range(len(nums)):
            if i > best_index:
                return False
            best_index = max(best_index, nums[i] + i)
        return True
