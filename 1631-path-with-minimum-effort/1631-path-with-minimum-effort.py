import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # solve with dijkstra's
        visited = set()
        i = 0
        j = 0

        # run dijkstra from heights[0][0]
        return self.dijkstra(i, j, heights, visited)

    def dijkstra(self, i, j, heights, visited):
        heap = [(0, i, j)]  # (effort, row, col), effort first so smallest pops

        while heap:
            effort, x, y = heapq.heappop(heap)

            # TODO #3: skip if (x, y) already visited, else mark it
            if (x, y) in visited:
                continue
            visited.add((x, y))
            #          if (x, y) is bottom-right, return effort
            if (x, y) == (len(heights) - 1, len(heights[0]) - 1):
                return effort

            directions = [(1,0), (0,1), (0,-1), (-1,0)]
            for d in directions:
                r = x + d[0]
                c = y + d[1]
                if 0 <= r <= len(heights) - 1 and 0 <= c <= len(heights[0]) - 1 and (r, c) not in visited:
                    diff = abs(heights[r][c] - heights[x][y])
                    heapq.heappush(heap, (max(effort, diff), r, c))  
