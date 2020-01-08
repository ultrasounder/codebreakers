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
                if currentSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                elif currentSum > 0:
                    right -= 1
        return []
                    
