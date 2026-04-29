class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cache1, cache2 = [0] * (n+1), [0] * (n+1)
        prefix_sum = list(accumulate([grid[j][0] for j in range(n)], initial=0))
        for i in range(1, n):
            dp = [[0] * (n+1) for _ in range(n+1)]
            for black in range(n+1):
                for k in range(n+1):
                    new_got = prefix_sum[black] - prefix_sum[k] if black > k else 0
                    dp[black][black] = max(dp[black][black], cache2[k] + new_got)
                total = 0
                for got in range(black+1, n+1):
                    total += grid[got-1][i]
                    dp[black][got] = cache1[~got] + total
            cache1 = list(accumulate([max(col) for col in reversed(dp)], max))
            cache2 = [max(dp[j][got] for j in range(n+1)) for got in range(n+1)]
            prefix_sum = list(accumulate([grid[j][i] for j in range(n)], initial=0))
        return cache1[-1]