"""34. Find First and Last Position of Element in Sorted Array"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def _findStartingIndex(self, nums, target):
            index = -1

            start = 0
            end = len(nums) - 1

            while start <= end:
                midpoint = start + (end - start) / 2
                
                if nums[midpoint] >= target:
                    end = midpoint - 1
                else:
                    start = midpoint + 1

                if nums[midpoint] == target:
                    index = midpoint






        def _findEndingIndex(self, nums, target):
            index = -1
            start = 0
            end = len(nums) - 1

            while start <= end:
                midpoint = start + (end - start) / 2

                if nums[midpoint] <= target:
                    end = midpoint + 1
                else:
                    start = midpoint - 1
                
                if nums[midpoint] == target:
                    index = midpoint


        result = []# create an array to hold the resultant indices of the first and last elements 
        result[0] = _findStartingIndex(nums, target)
        result[1] = _findEndingIndex(nums, target)

    