class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        modulo = 10**9+7
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1][0] = 0
        dp[n-1][n-1][1] = 1
        for i in range(n-2, -1, -1):
            if board[i][n-1] == 'X':
                break
            dp[i][n-1][0] = dp[i+1][n-1][0]+int(board[i][n-1])
            dp[i][n-1][1] = 1
        for j in range(n-2, -1, -1):
            if board[n-1][j] == 'X':
                break
            dp[n-1][j][0] = dp[n-1][j+1][0]+int(board[n-1][j])
            dp[n-1][j][1] = 1
        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                if board[i][j] != 'X':
                    max_sum = max(dp[i+1][j][0], dp[i][j+1][0], dp[i+1][j+1][0])
                    max_count = 0
                    if dp[i][j+1][0] == max_sum:
                        max_count += dp[i][j+1][1]
                    if dp[i+1][j][0] == max_sum:
                        max_count += dp[i+1][j][1]
                    if dp[i+1][j+1][0] == max_sum:
                        max_count += dp[i+1][j+1][1]
                    if max_sum != -1:
                        if board[i][j] != 'E':
                            dp[i][j][0] = max_sum+int(board[i][j])
                        else:
                            dp[i][j][0] = max_sum
                        dp[i][j][1] = max_count % modulo
        if dp[0][0][0] == -1:
            return [0, 0]
        else:
            return dp[0][0]