class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return None

        start = 0 # we will move all the zeros to the beginning of the list
        end = len(nums) - 1 # end will move all the Twos to the end of the list
        index = 0 # index will continue to move along the indices one after the other

        while index <= end and start < end:
            if nums[index] == 0:
                nums[index] = nums[start]
                nums[start] = 0
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[index] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                index += 1
                


