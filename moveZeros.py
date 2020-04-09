class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # index = 0
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] is not 0:
        #         nums[index + 1]  = nums[i]
        # for j in range(index, n):
        #     nums[j] = 0

        i, j = 0, 0
        n = len(nums)

        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        