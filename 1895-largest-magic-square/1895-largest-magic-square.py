class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])

        rSum = [[0] * n for _ in range(m)]
        cSum = [[0] * m for _ in range(n)]

        for y in range(m):
            for x in range(n):
                rSum[y][x] = (0 if x == 0 else rSum[y][x - 1]) + grid[y][x]
                cSum[x][y] = (0 if y == 0 else cSum[x][y - 1]) + grid[y][x]

        maxK = min(m, n)
        for k in range(maxK, 1, -1):
            for t in range(0, m - k + 1):
                for l in range(0, n - k + 1):
                    if self._check(grid, t, l, k, rSum, cSum):
                        return k
        return 1

    def _check(self, grid, t, l, k, rSum, cSum):
        b = t + k - 1
        r = l + k - 1
        s = rSum[t][r] - (0 if l == 0 else rSum[t][l - 1])
        d1 = 0
        d2 = 0
        for ki in range(k):
            rs = rSum[t + ki][r] - (0 if l == 0 else rSum[t + ki][l - 1])
            if rs != s:
                return False
            cs = cSum[l + ki][b] - (0 if t == 0 else cSum[l + ki][t - 1])
            if cs != s:
                return False
            d1 += grid[t + ki][l + ki]
            d2 += grid[t + ki][r - ki]
        return d1 == s and d2 == s