class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        xLo, yLo = float("inf"), float("inf")
        xHi, yHi = -float("inf"), -float("inf")
        for i, row in enumerate(grid):
            for j, b in enumerate(row):
                if b:
                    xLo, yLo = min(xLo, i), min(yLo, j)
                    xHi, yHi = max(xHi, i), max(yHi, j)
        return (xHi - xLo + 1) * (yHi - yLo + 1)