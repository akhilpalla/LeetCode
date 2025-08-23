class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        @cache
        def calc(r_lower, r_upper, c_lower, c_upper, left):
            if left == 1:
                if r_lower < r_upper:
                    if not any(grid[r_lower][c] for c in range(c_lower, c_upper + 1)):
                        return calc(r_lower + 1, r_upper, c_lower, c_upper, left)
                    if not any(grid[r_upper][c] for c in range(c_lower, c_upper + 1)):
                        return calc(r_lower, r_upper - 1, c_lower, c_upper, left)
                if c_lower < c_upper:
                    if not any(grid[r][c_lower] for r in range(r_lower, r_upper + 1)):
                        return calc(r_lower, r_upper, c_lower + 1, c_upper, left)
                    if not any(grid[r][c_upper] for r in range(r_lower, r_upper + 1)):
                        return calc(r_lower, r_upper, c_lower, c_upper - 1, left)
                return (r_upper - r_lower + 1) * (c_upper - c_lower + 1)
            else:
                best = M * N
                for s in range(1, left):
                    t = left - s
                    for r in range(r_lower, r_upper):
                        val = calc(r_lower, r, c_lower, c_upper, t) + calc(r + 1, r_upper, c_lower, c_upper, s)
                        if best > val: best = val
                    for c in range(c_lower, c_upper):
                        val = calc(r_lower, r_upper, c_lower, c, t) + calc(r_lower, r_upper, c + 1, c_upper, s)
                        if best > val: best = val
                return best
        return calc(0, M - 1, 0, N - 1, 3)
        