class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG = float('-inf')
        dp = [[[NEG] * (k + 1) for _ in range(n)] for _ in range(m)]
        v0 = grid[0][0]
        c0 = 1 if v0 > 0 else 0
        if c0 <= k:
            dp[0][0][c0] = v0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                cost = 1 if v > 0 else 0
                for c in range(cost, k + 1):
                    best = NEG
                    if i > 0 and dp[i-1][j][c-cost] != NEG:
                        best = max(best, dp[i-1][j][c-cost] + v)
                    if j > 0 and dp[i][j-1][c-cost] != NEG:
                        best = max(best, dp[i][j-1][c-cost] + v)
                    dp[i][j][c] = best
        ans = max(dp[m-1][n-1])
        return ans if ans != NEG else -1