# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #runtime O(N)
#         #space O(N)
#         new_s = ""
#         #remove white space and ignore case
#         for c in s:
#             if c.isalnum():
#                 new_s += c.lower() #if alphanumeric add it to new string and convert to lower

#         return new_s == new_s[::-1] #check if the start and end are the same

    
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #runtime O(N)
#         #space O(N)
#         new_s = ""
#         #remove white space and ignore case
#         for c in s:
#             if c.isalnum():
#                 new_s += c.lower() #if alphanumeric add it to new string and convert to lower

#         start, end = 0, len(new_s) - 1
#         while start < end:#as long as the start and end dont meet
#             if new_s[start] != new_s[end]: #compare the index of start wth end
#                 return False
#             start += 1
#             end -= 1
#         return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #runtime O(N)
        #space O(N)
        new_s = ""
        #remove white space and ignore case
        for c in s:
            if c.isalnum():
                new_s += c.lower() #if alphanumeric add it to new string and convert to lower
