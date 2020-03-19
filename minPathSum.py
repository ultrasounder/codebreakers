class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if len(grid) == 1:
            return 1
        if grid[0] == 0:
            return 1
        
        for i in range(n):
            for j in range(m):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[i-1][j-1]
