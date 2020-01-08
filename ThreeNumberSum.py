class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ##we sort the input array in ascending order. We can assume the fastest sorting algorithm out there(Quick sort)
        nums.sort()
        triplets = []# create an empty array to the hold the triplets
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
        return []
                    
