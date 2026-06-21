class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        def backtrack(r, c, current):
            if current == "":
                return True
            if board[r][c] != current[0]:
                return False
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


            original = board[r][c]
            board[r][c] = "#"
            if current[1:] == "":
                return True
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if backtrack(nr, nc, current[1:]):
                        return True
            board[r][c] = original
            return False

        for r in range(len(board)):
                for c in range(len(board[0])):    
                    if backtrack(r, c, word) is True:
                        return True
        return False


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna