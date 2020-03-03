import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort() # sorted O(nlogN)
        # return nums[len(nums)] - k


        Q = [] # creating a Queue
        for i in range(nums):
            Q.append(i)
            if(len(Q) > k):
                Q.remove()
        return Q.remove()
            



