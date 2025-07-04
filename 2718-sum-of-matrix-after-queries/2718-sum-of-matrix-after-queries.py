class Solution:
    def matrixSumQueries(self, n: int, queries: list) -> int:
        rowcol = [n, n]
        ans = 0
        seen = [0, 0]

        for t, i, v in reversed(queries):
            if not seen[t] & (1 << i):
                seen[t] |= 1 << i
                ans += v * rowcol[t]
                rowcol[t ^ 1] -= 1

        return ans