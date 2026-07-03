from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return the island count
        island_count = 0
        visited = set()

        # loop through every part 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # conduct bfs, marking lands as seen or not or water
                    visited.add((i, j))
                    self.bfs(grid, i, j, visited)
                    island_count += 1
        
        return island_count

    def bfs(self, grid, i, j, visited):
        visited.add((i,j))
        queue = deque([(i, j)])

        while queue:
            # current is a tuple that represents indices within the matrix 
            current = queue.popleft()

            for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_row = current[0] + direction[0]
                new_column = current[1] + direction[1]
                if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
                    if grid[new_row][new_column] == "1" and (new_row, new_column) not in visited:
                        # add it to the set and continue to conduct bfs from there
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna