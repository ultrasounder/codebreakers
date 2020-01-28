class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:[x])
        result = []
        for curr in intervals:
            if result and result[-1][1] >= curr[0]: # If there is an interval and if the previous end is greater than the current start
                result[-1][1] = max(result[-1][1], curr[1]) # we just swap
            else:
                result.append(curr) #No intervals just add the current 
            return result
            