class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1 take transpose
        # STep 2 reverse each row 

        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                # swap elements across upper half and lower half traingle
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(n):
            matrix[i].reverse()