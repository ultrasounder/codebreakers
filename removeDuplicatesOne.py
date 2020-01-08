### This uses Two pointer technique. Initialize two pointers. Iterate through the array, and at 
### array index, compare the values to every other value. If value not same , increment the pointer and 
### return the indices
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        i = 0

        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        