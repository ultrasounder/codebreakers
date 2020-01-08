class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Brute-Force technique that essentially loops over the entire array
        ### summing each element to the other to see if the sum equates the target
        ### Runtime O(N^2) spacetime O(1). Prior to the looping,it is essntial to check whether the arry is 
        ###is in some sorted order or not. If not, then use the quickest posible sort to sort the array.
        nums.sort() 
        if len(nums) < 2:
            return None

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                currentSum = nums[i] + nums[j]
                if currentSum == target:
                    return [i,j]

        return []

