def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        # arr = [2, 4, 5, 8]
        self.heap = nums[-k:]
        # self.heap = [4, 5, 8]
        self.k = k
        # self.k = 3
        heapq.heapify(self.heap)
        
        '''
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)
        '''
    
    
    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            headq.heappushpop(self.pool, val)
        return self.pool[0]
        # if we see a number smaller than the min in our heap, we will never need it again
        # if we see a number bigger than the min in our heap, we need to pop off the smallest element and push the element that was larger than the min
    