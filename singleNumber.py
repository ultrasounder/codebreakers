class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set() #initalize a hashset
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
        for i in seen:
            return i
