class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        for i in range(len(grid) - 1):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.add(i)
                    fresh.add(j)
                elif (grid[i][j] == 2):
                    rotten.add(i)
                    rotten.add(j)

        minutes = 0
        directions = [(0,1),(1,0), (-1,0),(0,-1)]
        while len(fresh) > 0:
            infected = set()
            for s in rotten:
                i = s[0] - '0'
                j = s[1] - '1'
                for direction in directions:
                    nextI = direction[0]
                    nextJ = direction[j]
                    if "" + nextI + nextJ in fresh:
                        fresh.remove("" + nextI + nextJ)
                        infected.add("" + nextI + nextJ)
                if len(infected) == 0:
                    return -1
                rotten = infected
                minutes += 1
        return minutes
        