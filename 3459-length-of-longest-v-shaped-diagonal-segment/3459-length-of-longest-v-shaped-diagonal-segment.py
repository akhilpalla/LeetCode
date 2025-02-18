class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        jorvexalin = grid
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        rot = [1, 3, 0, 2]
        dp = [None] * 4
        for d_idx, (dx, dy) in enumerate(dirs):
            dp0 = [[0] * m for _ in range(n)]
            dp1 = [[0] * m for _ in range(n)]
            if dx == 1 and dy == 1:
                for i in range(n - 1, -1, -1):
                    for j in range(m - 1, -1, -1):
                        if grid[i][j] == 2:
                            ni, nj = i + dx, j + dy
                            dp0[i][j] = 1 + (dp1[ni][nj] if ni < n and nj < m else 0)
                        else:
                            dp0[i][j] = 0
                        if grid[i][j] == 0:
                            ni, nj = i + dx, j + dy
                            dp1[i][j] = 1 + (dp0[ni][nj] if ni < n and nj < m else 0)
                        else:
                            dp1[i][j] = 0
            elif dx == 1 and dy == -1:
                for i in range(n - 1, -1, -1):
                    for j in range(m):
                        if grid[i][j] == 2:
                            ni, nj = i + dx, j + dy
                            dp0[i][j] = 1 + (dp1[ni][nj] if ni < n and nj >= 0 else 0)
                        else:
                            dp0[i][j] = 0
                        if grid[i][j] == 0:
                            ni, nj = i + dx, j + dy
                            dp1[i][j] = 1 + (dp0[ni][nj] if ni < n and nj >= 0 else 0)
                        else:
                            dp1[i][j] = 0
            elif dx == -1 and dy == 1:
                for i in range(n):
                    for j in range(m - 1, -1, -1):
                        if grid[i][j] == 2:
                            ni, nj = i + dx, j + dy
                            dp0[i][j] = 1 + (dp1[ni][nj] if ni >= 0 and nj < m else 0)
                        else:
                            dp0[i][j] = 0
                        if grid[i][j] == 0:
                            ni, nj = i + dx, j + dy
                            dp1[i][j] = 1 + (dp0[ni][nj] if ni >= 0 and nj < m else 0)
                        else:
                            dp1[i][j] = 0
            elif dx == -1 and dy == -1:
                for i in range(n):
                    for j in range(m):
                        if grid[i][j] == 2:
                            ni, nj = i + dx, j + dy
                            dp0[i][j] = 1 + (dp1[ni][nj] if ni >= 0 and nj >= 0 else 0)
                        else:
                            dp0[i][j] = 0
                        if grid[i][j] == 0:
                            ni, nj = i + dx, j + dy
                            dp1[i][j] = 1 + (dp0[ni][nj] if ni >= 0 and nj >= 0 else 0)
                        else:
                            dp1[i][j] = 0
            dp[d_idx] = (dp0, dp1)
        ans = 0
        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                ans = max(ans, 1)
                for d_idx, (dx, dy) in enumerate(dirs):
                    ni, nj = i + dx, j + dy
                    if not in_bounds(ni, nj):
                        continue
                    L1_max = dp[d_idx][0][ni][nj]
                    candidate = 1 + L1_max
                    ans = max(ans, candidate)
                    d_rot_idx = rot[d_idx]
                    d_rot = dirs[d_rot_idx]
                    for k in range(1, L1_max + 1):
                        ti, tj = i + k * dx, j + k * dy
                        si, sj = ti + d_rot[0], tj + d_rot[1]
                        if not in_bounds(si, sj):
                            continue
                        state = 0 if (k % 2 == 0) else 1
                        L2 = dp[d_rot_idx][state][si][sj]
                        candidate = 1 + k + L2
                        ans = max(ans, candidate)
        return ans