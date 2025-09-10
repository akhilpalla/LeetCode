class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        ans = 0
        MOD = 7 + 10**9

        if n==1: return 1

        dp = [0]*(n+1)
        dp[1] = 1
        window = 0

        for i in range(2,n+1):
            enter = i - delay
            exit_ = i - forget

            if enter>=1: window += dp[enter]
            if exit_>=1: window -= dp[exit_]

            dp[i] = window
        
        s = max(1,n-forget+1)
        ans = sum(dp[s:n+1]) % MOD
        return ans