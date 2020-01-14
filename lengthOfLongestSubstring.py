# class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
def lengthOfLongestSubstring(s):

    longest = start = end = 0
    contains = set()

    while end < len(s):
        if s[end] in contains:
            contains.remove(s[start])
            start += 1
        else:
            contains.add(s[end])
            end += 1
            longest = max(longest, end - start)
    return longest
    

       
s = "p w w k e w"

print(lengthOfLongestSubstring(s))

