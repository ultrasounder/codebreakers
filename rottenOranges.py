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
        freshOranges = set()
    q = Queue()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            curElement = grid[i][j]
            if curElement == 2:
                q.put((i,j))
            elif curElement == 1:
                freshOranges.add((i,j))
    time = 0
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while q.empty() == False and len(freshOranges) != 0:
        for k in range(q.qsize()):
            # do bfs and remove fresh oranges
            # queue will give us (i,j)
            i,j = q.get()
            # look at all neighbors and convert them to rotten oranges
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                continue
            # at this point, we know everything is in range
            if (i,j) in freshOranges:
                freshOranges.remove((i,j))
            for direction in directions:
                q.put((i + direction[0], j + direction[1]))
        time += 1
    if len(freshOranges) == 0:
        return time - 1
    return -1
    


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges(grid))


