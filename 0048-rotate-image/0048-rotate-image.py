# Brute: create a new array and place the elements where they belong in the new array
# (i,j)-->(j , n-1-i), this transformation do some mapping and derive
# T=S=N^2

# Optimal (inplace):
# transpose the array and reverse the each row 
# to transpsoe the array swap the non diagonal elements 
# T = 2nm
# S = 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # transposing the matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reversing each row of the matrix
        for i in range(n):
            matrix[i].reverse()
        