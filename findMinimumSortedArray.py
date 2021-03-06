# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

''''Classic Binary Search Problem''''

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return -1
        elif len(nums) == 1: # We do not even need this edge case check because your prgram automatically handles it
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = left + (right - left) // 2

            if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
                return nums[midpoint]
            elif nums[left] <= nums[midpoint] and nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return nums[left]
    
    '''
    Great solution. This runs great. Only have one suggestion which I pointed out above. Nice work!
    '''


        


