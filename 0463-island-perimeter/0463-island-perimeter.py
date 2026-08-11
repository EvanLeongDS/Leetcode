class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Strategy is to iterate through the grid if its land check how many are surrounded by land 
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # check the surrounding 4 borders
                    # an edge of the island automatically counts as +1 for the perimeter 
                    if i == 0:
                        perimeter += 1
                    if i == len(grid) - 1:
                        perimeter += 1
                    if j == 0:
                        perimeter += 1
                    if j == len(grid[0]) -1:
                        perimeter += 1
                    if i-1 >= 0 and grid[i-1][j] == 0:
                        perimeter += 1
                    if i + 1 <= len(grid) -1 and grid[i+1][j] == 0:
                        perimeter += 1
                    if j-1 >= 0 and grid[i][j-1] == 0:
                        perimeter += 1
                    if j+1 <= len(grid[0]) - 1 and grid[i][j+1] == 0:
                        perimeter += 1
                    
                
        return perimeter

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna