from collections import deque
lst = deque()
'''Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        # def dfs(matrix, row, column, prevVal, ocean = []): # why is the ocean initialize to empty list?


        #   #check necessary conditions 
        #     if row < 0 or column < 0 or row > len(matrix) - 1 or column > len(matrix) - 1: # this index should be matrix[0] for column
        #         return
        #     elif matrix[row][column] < prevVal:
        #         return

        #     elif ocean[row][column] == 1: # this is constantly going to be an empty ocean so we are going to get index out of bounds every time
        #         return        
      

        # #Process Cell

        #     ocean[row][column] = 1



        # #Call DFS as needed

        #     dfs(matrix, row, column, matrix[row][column], ocean) # why are we going to the same square and not the one below?
        #     dfs(matrix, row + 1, column, matrix[row][column], ocean)
        #     dfs(matrix, row, column - 1, matrix[row][column], ocean)
        #     dfs(matrix, row, column + 1, matrix[row][column, ocean])

        # pacific = []
        # atlantic = []


        
        # for col in range(len(matrix)):
        #     dfs(matrix, 0, col, float('-inf'), pacific)
        #     dfs(matrix, 0, col, float('-inf'), pacific)
        #     dfs(matrix, len(matrix) - 1, col, float('-inf'), atlantic)
            
        # for row in range(len(matrix)):
        #     dfs(matrix, row, 0, float('-inf'), pacific)
        #     dfs(matrix, row, len(matrix[0] - 1), float('-inf'), atlantic)
        # response = []

        # #iteratr thorugh the matrix and find common elements
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0] - 1)):
        #         if pacific[i][j] and  atlantic[i][j] == 1:
        #             lst.append(i)
        #             lst.append(j)
        #             response.append(lst)
        # return response

        '''
        Look through the comments and let me know if you are able to get it working. Your approach seems reasonable but I am not 
        exactly sure why you are initlizing the ocean to empty and never adding to it. Would be happy to look once this is changed.
        Just let me know. Keep it up!
        '''
def flow(grid):
    # 1. run dfs from all start nodes on the pacific side and add visited nodes to a set (if we can flow to them)
    # 2. do the same thing as step #1 but from the atlantic side
    # 3. take the overlap of the sets and return those coordinates
    pacificVisited = set()
    atlanticVisited = set()
    
    # top row
    for i in range(len(grid[0])):
        dfs(grid, i, 0, pacificVisited, 0)
        dfs(grid, i, len(grid) - 1, atlanticVisited, 0)
    
    # left side of grid
    for j in range(len(grid)):
        dfs(grid, 0, j, pacificVisited, 0)
        dfs(grid, len(grid[0]) - 1, j, atlanticVisited, 0)
    # get intersection of the sets
    return pacificVisited.intersection(atlanticVisited) # anything in both pacific and atlantic
          

def dfs(grid, i, j, seen, valueWeCameFrom):
    # edge cases/base cases                                  # water cannot flow to this
    if i < 0 or j < 0 or i == len(grid[0]) or j == len(grid) or grid[i][j] < valueWeCameFrom or (i,j) in seen:
        return
    # we know water can flow to it and we have not visited it before at this point
    seen.add((i, j))
    # perform dfs on all neighbors
    dfs(grid, i + 1, j, seen, grid[i][j])
    dfs(grid, i - 1, j, seen, grid[i][j])
    dfs(grid, i, j + 1, seen, grid[i][j])
    dfs(grid, i, j - 1, seen, grid[i][j])


grid = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(flow(grid))

'''
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''



