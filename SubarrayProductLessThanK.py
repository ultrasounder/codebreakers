# class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    prod = 1
    ans = 0
    left = 0

    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
        print(left, right)
    return ans


       
nums = [10, 5, 2, 6]
print(numSubarrayProductLessThanK(nums, 100))
