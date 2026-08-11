from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # strategy: iterate over the grid and do dfs to find the distance 
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        self.bfs(grid, queue)
    def bfs(self, grid, queue):
        # bfs helper function 
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if ni < 0 or ni >= len(grid) or nj <0 or nj >= len(grid[0]):
                    continue
                # skip the parts that aren't infinity
                if grid[ni][nj] != 2147483647:
                    continue
                grid[ni][nj] = grid[i][j] + 1
                queue.append((ni, nj))
                