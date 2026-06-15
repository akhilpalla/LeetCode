from collections import defaultdict as dd
class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = int(1e9 + 7)
        dp = dd(lambda : 0)
        dp[0] = 1
        for i in range(2,numPeople+1, 2):
            for j in range(0,i-1+1,2):
                l= j
                r= i-1 -j -1
                dp[i]+=dp[l] * dp[r]
                dp[i] %=MOD
        return dp[numPeople]