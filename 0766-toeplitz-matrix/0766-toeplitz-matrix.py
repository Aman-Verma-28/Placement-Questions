class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pointer = 0
        rows = len(matrix)
        columns = len(matrix[0])
        
        while pointer < columns:
            row = 0
            column = pointer
            val = matrix[row][column]
            while row<rows and column<columns:
                if matrix[row][column]!=val:
                    return False
                row += 1
                column += 1
            pointer += 1
        
        pointer = 1
        
        while pointer < rows:
            row = pointer
            column = 0
            val = matrix[row][column]
            while row<rows and column<columns:
                if matrix[row][column]!=val:
                    return False
                row += 1
                column += 1
            
            pointer += 1
        
        return True
            