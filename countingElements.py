class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        count = 0
        seen = set()
        for i in arr:
            seen.add(i)
        #for each element i, check if x+1 is in the array
        for i in arr:
            if i+1 in arr:
                count += 1
        return count