class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfsMark(grid, i, j)
                    count += 1
        return count
        
        
        def dfsMark(grid, row, column):
            if row < 0 or column < 0 or row > len(grid) - 1 or column > len(grid) - 1: # this check here should be grid[0] because we are checking column, not row
                return
            if grid[row][column] == '0':
                return
            
            grid[row][column] = '0' # process a cell

            #call DFS
            dfsMark(grid, row, column - 1)#DFS left cell
            dfsMark(grid, row, column + 1)#DFS right cell
            dfsMark(grid, row - 1, column)#top
            dfsMark(grid, row + 1, column)#bottom
        '''
        Nice solution. This is exactly the optimal way of thinking about this problem. Make sure you are careful with this checks
        because this can actually be a pretty diffcult thing to debug if you are asked to run your coed in an interview. Excellent work!
        '''






