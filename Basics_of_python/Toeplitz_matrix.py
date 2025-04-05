class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return True
        cols = len(matrix[0])
    
        i = 0
        while i < rows - 1:
            j = 0
            while j < cols - 1:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                j += 1
            i += 1
        return True
       
# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
solution = Solution()
print(solution.isToeplitzMatrix(matrix))  # Output: True