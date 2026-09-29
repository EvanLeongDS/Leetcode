from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0 
        visited = set()

        # loop over all the different islands and if they are not in visited call bfs on it 
        m = len(grid)
        n = len(grid[0])

        # iterate over the entire grid 
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == "1":
                    num_islands += 1 
                    self.bfs(grid, i, j, visited)
        return num_islands
    
    def bfs(self, grid, i, j, visited):
        queue = deque()
        queue.append((i, j))
        visited.add((i, j))
        while queue:
            x = queue.popleft()
            # check all surrounding areas 
            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
            for direction in directions:
                r = x[0] + direction[0]
                c = x[1] + direction[1]
                if 0 <= r <= (len(grid) -1) and 0 <= c <= (len(grid[0]) - 1):
                    if grid[r][c] == "1" and (r, c) not in visited: # make it a string because its not an int in the grid 
                        visited.add((r, c))
                        queue.append((r, c))