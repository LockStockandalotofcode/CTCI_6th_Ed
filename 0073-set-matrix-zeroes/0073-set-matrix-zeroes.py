class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        # Check if row or column is zero, they need to be made zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(columns))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Extracting the 0 elements' positions
        # and saving in the first row and column
        for i in range(1, rows): # by default range() starts from 0, thus explicitly stating; matrix indexed from 0 to len-1
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # making the required rows and columns (other than first row and column) 0
        for i in range(1, rows):
                for j in range(1, columns):
                    if matrix[0][j]==0 or matrix[i][0]==0:
                        matrix[i][j] = 0
        
        # Handle first row and first column
        if first_row_zero:
            for j in range(columns):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0