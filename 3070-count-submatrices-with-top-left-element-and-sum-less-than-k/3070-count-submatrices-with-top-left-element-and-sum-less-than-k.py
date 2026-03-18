class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        prefix_sum = [[0] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                top = prefix_sum[i - 1][j] if i > 0 else 0
                left = prefix_sum[i][j - 1] if j > 0 else 0
                top_left = prefix_sum[i - 1][j - 1] if i > 0 and j > 0 else 0

                prefix_sum[i][j] = top + left - top_left + grid[i][j]

                if prefix_sum[i][j] <= k:
                    count += 1

        return count