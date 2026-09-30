from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        visited = set()
        
        m = len(grid)
        n = len(grid[0])
        # iterate over the grid if the grid is a 1 and is not in visited call bfs 
        area_list = [] # for debugging
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.bfs(grid, i, j, visited)
                    area_list.append(area)
                    max_area = max(max_area, area)
        print(area_list)
        return max_area

    def bfs(self, grid, i, j, visited):
        visited.add((i, j))
        queue = deque()
        queue.append((i, j))
        area = 1 

        while queue:
            x = queue.popleft()
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for direction in directions:
                newx = x[0] + direction[0]
                newy = x[1] + direction[1]

                # check if in bounds and not visited
                if 0 <= newx <= len(grid) - 1 and 0 <= newy <= len(grid[0]) - 1 and (newx, newy) not in visited and grid[newx][newy] == 1:
                    queue.append((newx, newy))
                    visited.add((newx, newy))
                    area += 1 

        return area 
