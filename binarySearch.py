class Solution:
    
    def search(self, nums: List[int], target: int) -> int:



        def binarySearchHelper(nums, target, low, hi):

            while low <= hi:

                pivot = low + (hi - low) // 2

                if nums[pivot] == target:
                    return pivot
                if nums[pivot] < target:
                    hi = pivot - 1
                else:
                    lo = pivot + 1
            return -1

        return binarySearchHelper(nums, target, 0, len(nums) -1)