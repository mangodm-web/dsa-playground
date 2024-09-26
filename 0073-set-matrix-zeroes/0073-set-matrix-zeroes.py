class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_to_change, column_to_change = set(), set()

        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    row_to_change.add(row)
                    column_to_change.add(column)
        
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if row in row_to_change or column in column_to_change:
                    matrix[row][column] = 0
