class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]* (m+1) for _ in range(n+1)]
        m = len(text2)
        n = len(text1)

        for i in range(n):
            for j in range(m):
                if text1[i+1] == text2[i+1]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

    