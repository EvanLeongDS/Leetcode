class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check for repetition across rows
        seen = []
        for row in board:
            for number in row:
                if number == ".":
                    pass
                elif number not in seen:
                    seen.append(number)
                else:
                    return False
            seen = []

        # check for reptition across columns
        for column in zip(*board):
            for number in column:
                if number == ".":
                    pass
                elif number not in seen:
                    seen.append(number)
                else:
                    return False
            seen = []
        
        # check the blocked off grids

        # Establish that there are 9 blocks
        for block_row in range(3):
            for block_col in range(3):
                seen = []
                # walk through the 9 numbers in each block
                for row_walker in range(3):
                    for col_walker in range(3):
                        number = board[block_row * 3 + row_walker][block_col * 3 + col_walker]
                        if number == ".":
                            pass
                        elif number not in seen:
                            seen.append(number)
                        else:
                            return False 

        # We have passed all checks, return true
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna