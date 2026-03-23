class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n_r = len(grid); n_c = len(grid[0])
        dp_max = [[0]*n_c for _ in range(n_r)]
        dp_min = [[0]*n_c for _ in range(n_r)]
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        for r in range(1, n_r):
            dp_max[r][0] = dp_min[r][0] = grid[r][0]*dp_max[r-1][0]
        for c in range(1, n_c):
            dp_max[0][c] = dp_min[0][c] = grid[0][c]*dp_max[0][c-1]
        for r in range(1, n_r):
            for c in range(1, n_c):
                dp_max[r][c] = max(dp_max[r-1][c]*grid[r][c], dp_max[r][c-1]*grid[r][c], dp_min[r-1][c]*grid[r][c], dp_min[r][c-1]*grid[r][c])
                dp_min[r][c] = min(dp_max[r-1][c]*grid[r][c], dp_max[r][c-1]*grid[r][c], dp_min[r-1][c]*grid[r][c], dp_min[r][c-1]*grid[r][c])
        if dp_max[n_r-1][n_c-1] < 0: return -1
        return dp_max[n_r-1][n_c-1]%(10**9+7)