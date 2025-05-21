# Brute
# iterate through the matrix and when you see 0 set row and col to -1 where you see 1, because if we set to 0 we dont know which are initial zeros
# and in the final iteration convert -1 to 0

# T = (nm)(n+m) + (nm)
# S = 1

# Better
# we are getting n^3 bcoz of marking immediately after encountering 0, instead carry an extra array for column and row to mark which row and col should be changed and later convert them to 0 
# T = 2mn
# S = n+m

# Optimal
# T cannot be reduced because we have to visit all elements but space we can reduce to O(1)
# instaed of extra array to keep track of 0 do it inplace
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        col0 = 1
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark i-th row:
                    matrix[i][0] = 0

                    # mark j-th column:
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        #step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix
        
# T = 2nm
# S = 1