class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # establish fundamental variables
        safe = set() # if you are in safe you are not getting changed up 
        # run dfs from the border 
        m, n = len(board), len(board[0])

         # iterate through the top row left to right
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(board, 0, j, safe)

        # iterate through leftmost column top down
        for i in range(1, m): # don't iterate on row 0 since we already did that
            if board[i][0] == "O":
                self.dfs(board, i, 0, safe)
        
        # iterate through rightmost column top down
        for i in range(m):
            if board[i][n-1] == "O":
                self.dfs(board, i, n - 1, safe)

        # iterate through the bottom row
        for j in range(n):
            if board[m-1][j] == "O":
                self.dfs(board, m - 1, j, safe)

        # loop through everything and change whatever is not in the safe set 
        print(safe)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"
        
    def dfs(self, board, r, c, safe):
        # base case
        if (r, c) in safe:
            return
        
        # add the coords to safe 
        safe.add((r, c))

        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        for neighbor in directions:
            new_x = r + neighbor[0]
            new_y = c + neighbor[1]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == "O":
                    self.dfs(board, new_x, new_y, safe)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna