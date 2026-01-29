class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxSquareSide = 0 #our current max square side length
        for val in matrix[0]:
            if val == "1":
                maxSquareSide = 1
                break
        if maxSquareSide == 0:
            for i in range(m):
                if matrix[i][0] == "1":
                    maxSquareSide = 1
                    break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    matrix[i][j] = str(min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1])) + 1)
                if int(matrix[i][j]) > maxSquareSide:
                    maxSquareSide = int(matrix[i][j])
        return maxSquareSide**2