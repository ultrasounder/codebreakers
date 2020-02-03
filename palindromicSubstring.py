class Solution:
    def longestPalindrome(self, s: str) -> str:
  
        currentLongest = [0, 1] # values of starting index and ending index of the longest palindromic substring
        """ew are initializing starting index to be the first character"""
        for i in range(1, len(s)):
            odd = self.getLongestPalindromeFromgetLongestPalindromeFrom(s, i-1, i+1)# Left index and right index
            even = self.getLongestPalindromeFromgetLongestPalindromeFrom(s, i, i+1)
            longest = max(odd, even, key= lambda x:x[1] - x[0])
            currentLongest = max(longest, currentLongest, key= lambda x: x[1]-x[0])
        return str[currentLongest[0]:currentLongest[1]] # variable name is s, not str. Very minor mistake


    def getLongestPalindromeFrom(self, s, left_index, right_index):
        while left_index >= 0 and right_index < len(s):
            if s[left_index] != s[right_index]:
                break
            left_index -= 1
            right_index += 1
        return [left_index + 1, right_index]
        '''
        Overall, your solution is great. Perfect use of the helper method. One case that we do not cover is
        if our string is even and starts on the first character. For example "aa" would only return "a". We can fix 
        this by starting the for loop at 0. This is because your even looks head and not behind, so we lose the 
        case of a even numbered palindrome if we do not start at 0. I was trying to illustrate during the lesson that we do
        not check the first character when looking for an odd palindrome because the answer will always be 1. We do need to check
        for the even case because this could give us a new longest substring. 
        '''



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




