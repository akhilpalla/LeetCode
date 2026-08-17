class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        length = len(stoneValue)
        if length == 1:
            return 0
        
		# Calculate sum
        s = [0 for _ in range(length)]
        s[0] = stoneValue[0]
        for i in range(1, length):
            s[i] = s[i-1] + stoneValue[i]
		
		# dp for best value, best_cut for where is the cut in (i, j), i, j inclusive
        dp = [[0 for _ in range(length)] for _ in range(length)]
        best_cut = [[0 for _ in range(length)] for _ in range(length)]
        
        for i in range(0, length-1):
            dp[i][i+1] = min(stoneValue[i], stoneValue[i+1])
            best_cut[i][i+1] = i
            
        for t in range(2, length):
            for i in range(0, length-t):
                tmp_dp = 0
                tmp_cut = 0
                left_bound = best_cut[i][i+t-1]
                if left_bound > i:
                    left_bound -= 1
                right_bound = best_cut[i+1][i+t]
                if right_bound < i+t-1:
                    right_bound += 1
                    
                for k in range(left_bound, 1+right_bound):
                    s1 = s[k] - s[i-1] if i > 0 else s[k]
                    s2 = s[i+t] - s[k]
                    if s1 < s2:
                        tmp = s1 + dp[i][k]
                        if tmp > tmp_dp:
                            tmp_dp = tmp
                            tmp_cut = k
                    elif s1 > s2:
                        tmp = s2 + dp[k+1][i+t]
                        if tmp > tmp_dp:
                            tmp_dp = tmp
                            tmp_cut = k
                    else:
                        tmp1 = s1 + dp[i][k]
                        tmp2 = s2 + dp[k+1][i+t]
                        if tmp1 > tmp_dp:
                            tmp_dp = tmp1
                            tmp_cut = k
                        if tmp2 > tmp_dp:
                            tmp_dp = tmp2
                            tmp_cut = k
        
                dp[i][i+t] = tmp_dp
                best_cut[i][i+t] = tmp_cut
                
        return dp[0][length-1]