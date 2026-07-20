class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        zero_set = set() # I will use this to keep track of which zeros were in the original matrix and which ones were edited 

        # iterate to look for the original 0s
        for i in range(m + 1):
            for j in range(n + 1):
                if matrix[i][j] == 0:
                    zero_set.add((i, j))

        for i in range(m+1):
            for j in range(n+1):
                if matrix[i][j] == 0 and (i,j) in zero_set:
                    for k in range(m+1):
                        matrix[k][j] = 0
                    for l in range(n+1):
                        matrix[i][l] = 0
      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna