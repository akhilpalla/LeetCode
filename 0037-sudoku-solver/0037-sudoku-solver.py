class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle in-place.
        """
        self.solve(board)

    def solve(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in '123456789':  # Try numbers 1 to 9
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'  # Backtrack
                    return False  # No valid number found, need to backtrack
        return True

    def isValid(self, board: List[List[str]], row: int, col: int, c: str) -> bool:
        """
        Checks if placing the number 'c' in the position (row, col) is valid.
        """
        for i in range(9):
            if board[i][col] == c:  # Check the column
                return False
            if board[row][i] == c:  # Check the row
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:  # Check the 3x3 box
                return False
        return True

# total there are n^2 squares and each sqaure will have 9 options ==> 9^(n^2) 
# S = 1