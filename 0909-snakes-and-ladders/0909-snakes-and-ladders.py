class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n: int = len(board)
        dp: list[list[int]] = [[401] * n for _ in range(n)]
        cur_nodes: list[tuple[int, int]] = [(0, 0)]
        next_nodes: list[tuple[int, int]] = []
        dp[0][0] = 0
        while cur_nodes:
            for row, col in cur_nodes:
                path: int = dp[row][[col, n - col - 1][row & 1]]
                for move in range(1, 7):
                    next_ceil: int = row * n + col + move
                    if next_ceil >= n * n: continue
                    next_row: int = next_ceil // n
                    next_col: int = next_ceil % n
                    if board[next_row][[next_col, n - next_col - 1][next_row & 1]] != -1:
                        next_ceil: int = board[next_row][[next_col, n - next_col - 1][next_row & 1]] - 1
                        next_row_jump: int = next_ceil // n
                        next_col_jump: int = next_ceil % n
                        if path + 1 < dp[next_row_jump][[next_col_jump, n - next_col_jump - 1][next_row_jump & 1]]:
                            dp[next_row_jump][[next_col_jump, n - next_col_jump - 1][next_row_jump & 1]] = path + 1
                            next_nodes.append((next_row_jump, next_col_jump))
                    elif path + 1 < dp[next_row][[next_col, n - next_col - 1][next_row & 1]]:
                        dp[next_row][[next_col, n - next_col - 1][next_row & 1]] = path + 1
                        next_nodes.append((next_row, next_col))
            cur_nodes = next_nodes
            next_nodes = []
        return [dp[n - 1][[n - 1, 0][(n - 1) & 1]], -1][dp[n - 1][[n - 1, 0][(n - 1) & 1]] == 401]