
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # establish fundamental variables 
        fresh = 0 # when there is 0 fresh ones we done 
        queue = deque()
        # iterate through the grid to look for rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1 

        minutes, fresh = self.bfs(grid, queue, fresh)
        return minutes if fresh == 0 else -1

    def bfs(self, grid, queue, fresh):
        # run bfs as long as the queue is there and we have fresh oranges 
        minutes = 0 
        while queue and fresh > 0:
            for _ in range(len(queue)):
                current = queue.popleft()
                for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_row = current[0] + direction[0]
                    new_column = current[1] + direction[1]
                    if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
                        if grid[new_row][new_column] == 1:
                            fresh -= 1
                            grid[new_row][new_column] = 2
                            queue.append((new_row, new_column))
            minutes += 1
        return minutes, fresh


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna