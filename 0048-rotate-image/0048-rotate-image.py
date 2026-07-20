class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the matrix 
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[i][j]
                temp2 = matrix[j][i]
                matrix[i][j] = temp2
                matrix[j][i] = temp
 
        # reverse each row I can do this with two pointers right?
        for row in matrix:
            i = 0 
            j = len(row) - 1
            while i < j:
                # save then switch
                a = row[i]
                b = row[j]
                row[i] = b
                row[j] = a
                i += 1
                j -= 1

        