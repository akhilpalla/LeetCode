class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        max_area = 0
        for row in matrix:
            row.sort(reverse=True)
            for j, h in enumerate(row):
                max_area = max(max_area, h * (j + 1))
        return max_area