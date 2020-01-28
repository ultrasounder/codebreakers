class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:[x])
        result = []
        for curr in intervals:
            if result and result[-1][1] >= curr[0]:
                result[-1][1] = max(result[-1][1], curr[1])
            else:
                result.append(curr)
            return result
            