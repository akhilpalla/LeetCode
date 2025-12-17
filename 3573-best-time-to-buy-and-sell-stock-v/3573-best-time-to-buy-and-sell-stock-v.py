class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp_prev = [[-inf for _ in range(k+1)] for _ in range(3)]
        dp_prev[2][0] = 0

        n = len(prices)

        for i in range(1, n+1):
            dp = [[-inf for _ in range(k+1)] for _ in range(3)]
            for j in range(k+1):
                dp[0][j] = max(dp_prev[0][j], dp_prev[2][j] - prices[i-1])  # hold +1: stay or buy
                dp[1][j] = max(dp_prev[1][j], dp_prev[2][j] + prices[i-1])  # hold -1: stay or sell
                if j == 0:
                    dp[2][j] = dp_prev[2][j]  # This is correct
                else:
                    dp[2][j] = max(dp_prev[2][j], dp_prev[0][j-1] + prices[i-1], dp_prev[1][j-1] - prices[i-1])            
            dp_prev = dp
        return max(dp_prev[2][j] for j in range(k+1))