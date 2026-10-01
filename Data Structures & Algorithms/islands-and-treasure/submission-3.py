from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        queue = deque()

        # start from every treasure
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            x = queue.popleft()
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                r = x[0] + dr
                c = x[1] + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == inf:
                    grid[r][c] = grid[x[0]][x[1]] + 1   # one more than the cell I came from
                    queue.append((r, c))