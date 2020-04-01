class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])
        dp = [0] * m

        if len(grid) == 1:
            return 1
        if grid[0] == 0:
            return 1
        
        for i in range(n):
            for j in range(m):
                dp[i][j] += min(grid[i-1][j], grid[i][j-1])
        return dp[i-1][j-1]
        
        '''
        You have the right idea with this one. You want to use DP to build off previously explored paths.
        However, you are writing to the same grid you are reading from. This messes up future DP entries
        because some numbers are larger (because you added them) than what they should be when added to the DP
        grid. To fix this, I would use nearly the same loops but with a new grid initialized with all 0s. Let me
        know how this goes!
        '''
        
        '''Added the dp array to - AV '''

