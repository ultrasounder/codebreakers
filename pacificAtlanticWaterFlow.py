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
        
        
        def dfs(matrix, row, column, prevVal, ocean = []):


          #check necessary conditions 
            if row < 0 or column < 0 or row > len(matrix) - 1 or column > len(matrix) - 1:
                return
            elif matrix[row][column] < prevVal:
                return

            elif ocean[row][column] == 1:
                return        
      

        #Process Cell

        ocean[row][column] = 1



        #Call DFS as needed

        dfs(matrix, row, column, matrix[row][column], ocean)
        dfs(matrix, row + 1, column, matrix[row][column], ocean)
        dfs(matrix, row, column - 1, matrix[row][column], ocean)
        dfs(matrix, row, column + 1, matrix[row][column, ocean])


