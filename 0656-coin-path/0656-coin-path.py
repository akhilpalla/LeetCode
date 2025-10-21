class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        @cache
        def dp(i):
            if coins[i-1] == -1:
                return float('inf'),None
            if i == n:
                return coins[i-1],tuple([n])
            res = float('inf')
            respath = None
            for j in range(i+1,min(i+maxJump,n)+1):
                cost,path = dp(j)
                if cost < res or (cost == res and path is not None and path < respath):
                    res = cost
                    respath = path
            if res==float('inf'): return float('inf'),None
            return res + coins[i-1], tuple([i]+list(respath))
        cost,path = dp(1)
        if cost<float('inf'):return list(path)
        else:return []