class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # intialize an empty dict to hold the numbers
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in map:
                return [map[potentialMatch], i]
            map[num] = i
           ## This one looks great! Nice job making a new variable to store the answer versus computing it twice. Variable names
           ## look solid and your efficiency is spot on. You make great use of the enumerate function as well
