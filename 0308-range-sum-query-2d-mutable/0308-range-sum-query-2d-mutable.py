class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.acc = [[0] + list(accumulate(i)) for i in matrix]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.acc[row] = [0] + list(accumulate(self.matrix[row]))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            sum += self.acc[i][col2+1] - self.acc[i][col1]
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)