class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        xs = x                   
        ys = y                   
        xf = x + k - 1           
        yf = y + k - 1           

        while xs < xf:
            for col in range(ys, yf + 1):
                grid[xs][col], grid[xf][col] = grid[xf][col], grid[xs][col]
            xs += 1
            xf -= 1

        return grid