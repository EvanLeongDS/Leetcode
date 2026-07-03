class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #final solution
        pacific_list = set()
        atlantic_list = set()
        # loop through the perimeter of the grid
        # m: row count, n is column count
        m, n = len(heights), len(heights[0])

        # iterate through the top row left to right
        for i in range(n):
            self.dfs_pacific(heights, 0, i, pacific_list)
        # iterate through leftmost column top down
        for j in range(1, m): # don't iterate on row 0 since we already did that
            self.dfs_pacific(heights, j, 0, pacific_list)
        
        # iterate through rightmost column top down
        for j in range(m):
            self.dfs_atlantic(heights, j, n - 1, atlantic_list)
        # iterate through the bottom row
        for i in range(n):
            self.dfs_atlantic(heights, m - 1, i, atlantic_list)

        print(pacific_list)
        print(atlantic_list)

        result = pacific_list.intersection(atlantic_list)
        return [list(cell) for cell in result]
    
    def dfs_pacific(self, heights, r, c, pacific_list):
        # conduct dfs to see if pacific crosses to atlantic and vice versa
        pacific_list.add((r, c))
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for neighbor in directions:
            new_x = r + neighbor[0]
            new_y = c + neighbor[1]

            # check range limits
            if 0 <= new_x < len(heights) and 0 <= new_y < len(heights[0]):

                # check if its not in visited and do reverse flow
                if (new_x, new_y) not in pacific_list and heights[r][c] <= heights[new_x][new_y]:
                    self.dfs_pacific(heights, new_x, new_y, pacific_list)

    def dfs_atlantic(self, heights, r, c, atlantic_list):
        # conduct dfs to see if pacific crosses to atlantic and vice versa
        atlantic_list.add((r, c))
        
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for neighbor in directions:
            new_x = r + neighbor[0]
            new_y = c + neighbor[1]

            # check range limits
            if 0 <= new_x < len(heights) and 0 <= new_y < len(heights[0]):

                # check if not in visited and conduct reverse flow
                if (new_x, new_y) not in atlantic_list and heights[r][c] <= heights[new_x][new_y]:
                    self.dfs_atlantic(heights, new_x, new_y, atlantic_list)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna