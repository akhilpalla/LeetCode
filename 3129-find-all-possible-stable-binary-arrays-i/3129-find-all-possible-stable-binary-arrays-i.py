class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
        dp = [[[[0] * (limit+1) for i in range(2)] for j in range(one+1)] for k in range(zero+1)]
        dp[0][0][0][0] = 1
        dp[0][0][1][0] = 1

        for i in range(zero+1):
            for j in range(one+1):
                for k in range(1, limit+1): 
                    
                    if i >= k:
                        if k == 1:
                            dp[i][j][0][k] += sum(dp[i-1][j][1])
                        else:
                            dp[i][j][0][k] += dp[i-1][j][0][k-1]
                        
                    if j >= k:
                        if k == 1:   
                            dp[i][j][1][k] += sum(dp[i][j-1][0])
                        else:
                            dp[i][j][1][k] += dp[i][j-1][1][k-1]
                        
        return sum(dp[-1][-1][0] + dp[-1][-1][1]) % (10**9 + 7)
                