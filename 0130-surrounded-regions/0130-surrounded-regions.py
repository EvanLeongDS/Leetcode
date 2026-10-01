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
        
        # iterate through the whole board, whichever o is not safe becomes X
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"
        
    def dfs(self, board, i, j, safe):
        safe.add((i, j))
        directions = [(1,0), (0,1), (0,-1), (-1,0)]

        for direction in directions:
            newx = i + direction[0]
            newy = j + direction[1]

            if 0 <= newx <= len(board) - 1 and 0 <= newy <= len(board[0]) - 1 and board[newx][newy] == "O" and (newx, newy) not in safe:
                safe.add((newx, newy))
                self.dfs(board, newx, newy, safe)
