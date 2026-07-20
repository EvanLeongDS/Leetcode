class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        # row pointers
        top = 0
        bottom = len(matrix) - 1 
        # column pointers
        left = 0 
        right = len(matrix[0]) - 1
        print(bottom, right)

        # push inward once the while conditions are not true
        while top <= bottom and left <= right:
            # top row 
            for column in range(left, right + 1):
                output.append(matrix[top][column])
            top += 1
            # rightmost column
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1 
            # bottom row
            if top <= bottom:
                for column in range(right, left -1, - 1):
                    output.append(matrix[bottom][column])
                bottom -= 1
            # left most column 
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1
        
        return output