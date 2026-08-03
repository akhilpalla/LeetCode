class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            score = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                score += stoneValue[i + k - 1]
                dp[i] = max(dp[i], score - dp[i + k])
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"