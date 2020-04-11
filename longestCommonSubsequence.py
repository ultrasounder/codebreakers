class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]* (m+1) for _ in range(n+1)] # variables referenced before assignment
        m = len(text2)
        n = len(text1)

        for i in range(n): # ranges will throw out of bounds errors
            for j in range(m):
                if text1[i+1] == text2[i+1]: # i and not j for the second string
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
'''
You did a good job of using a grid and coming up with the recurrence relation. There are a few errors that will happen at runtime.
We also want to make sure we are actually looping through the entire grid which we are not doing here. I have some code below
that I hope flushes out some of the details. I just made some small tweaks to your code. Also remember that i will correspond to text2
and that j will corspond to text1. This is almost an inversion of logic, but if you look at how the grid is initalized, it should 
actually make sense. As I mentioned, your recurrence is exactly what we want it to be. The starting edges are all 0s because we are
matching 0 characters at that point. When we see matching character, we know we need to "burn" up a charaacter from each string and
so look at the square diagonal to where we were. When we do not have a match, we need to account for either of the strings (bot not
both) "burning" a character. We keep repeating this until we get to the end of the string, or the lower right hand corner of our
grid. Let me know if any of this doesn't make sense I we can hopp on a call to talk about it

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]* (len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
'''
