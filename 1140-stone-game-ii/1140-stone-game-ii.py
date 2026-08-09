from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def dp(i, M):
            if i >= n:
                return 0
            res = float('-inf')
            prefix_sum = 0
            for k in range(2*M):
                if i + k < n: 
                    prefix_sum += piles[i+k]
                    res = max(res, prefix_sum-dp(i+k+1, max(M, k+1)))
                else:
                    break
            return res
        
        return (sum(piles) + dp(0, 1)) // 2