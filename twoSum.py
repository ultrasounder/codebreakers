class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # intialize an empty dict to hold the numbers
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in map:
                return [map[potentialMatch], i]
            map[num] = i
            