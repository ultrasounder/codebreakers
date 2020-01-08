# [1 2 3 4 5 6 7]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### We will attempt to solve this problem using the two-pointer technique. There
        ### are two other techniques available, using two FOR loops which is O(n^2) run-time, O(1) spacetime
        ### Using Hasmap look-up which is O(N) run-time and O(N) space-time(as we use an auxiliary DS). 
        ### The run-time for this version would be O(nlogn) and O(1) resp.
        leftPointer = 0
        rightPointer = len(nums) - 1
        if len(nums) < 2:
            return None

        while leftPointer < rightPointer:
            currentSum = nums[leftPointer] + nums[rightPointer]
            if target == currentSum:
                return [leftPointer, rightPointer]
            elif currentSum < target:
                leftPointer += 1
            elif currentSum > target :
                rightPointer -= 1

        return []

  
                

                

