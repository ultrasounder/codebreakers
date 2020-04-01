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
        
        '''
        Edit 2: the recurrence makes sense, we just want to make sure we are adding to our grid properly. Below I listed a concise
        way to do so. Basically we look at our dp grid to see the best route so far, and add in the square we are about to explore.
        By making the dp one bigger than the grid, we can save a lot of code and index out of bounds. Let me know if any of this
        doesn't make sense and we can discuss!
        
        class Solution:
         def minPathSum(self, grid):
                m, n = len(grid[0]), len(grid)
                dp = [[float('inf')] * (m + 1) for i in range(n + 1)]
                dp[0][1] = dp[1][0] = 0

                for i in range(1, n + 1):
                    for j in range(1, m + 1):
                        dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
                return dp[-1][-1]
        '''
        
        '''Added the dp array to - AV '''

