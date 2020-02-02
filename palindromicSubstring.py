class Solution:
    def longestPalindrome(self, s: str) -> str:

        currentLongest = [0, 1] # values of starting index and ending index of the longest palindromic substring



        # n = len(s)
        # for length in range(n)[::-1]:
        #     for i in range(n - length):
        #         sub = s[i: i+length + 1]
        #         if sub == sub[::-1]:
        #             return sub
        # return ''


    #     if s == None or len(s) < 1:
    #         return " "
    #     start = 0
    #     end = 0

    #     for i in range(len(s) - 1):
    #         len1 = expandFromMiddle(s, i, i)
    #         len2 = expandFromMiddle(s, i, i + 1)
    #         length = max(len1, len2)
    #         if length > end - start:
    #             start = i - ((length - 1) / 2)
    #             end = i + (length / 2)

    #     return s[::+1]

    # def expandFromMiddle(s, left, right):
    #     if s == 0 or left > right:
    #         return 0
    #     while (left >= 0 and right < len(s) and s[left] == s[right]):
    #         left -= 1
    #         right += 1

    #     return right - left - 1




