from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = self.bfs(grid, i, j , visited)
                    if area > max_area:
                        max_area = area
        return max_area
    
    def bfs(self, grid, i, j, visited):
        # establish queue and area metric
        visited.add((i, j))
        queue = deque([(i, j)])
        area = 1 

        # count islands 
        while queue:
            current = queue.popleft()

            for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_row = current[0] + direction[0]
                new_column = current[1] + direction[1]
                if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
                    if grid[new_row][new_column] == 1 and (new_row, new_column) not in visited:
                        # add it to the set and continue to conduct bfs from there
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column))
                        area += 1
        return area
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna