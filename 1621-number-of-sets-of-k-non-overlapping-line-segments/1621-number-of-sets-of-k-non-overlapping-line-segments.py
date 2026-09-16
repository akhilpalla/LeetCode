class Solution:
    def numberOfSets(self, n, k):
        mod = 10**9+7
        @lru_cache(None)
        def dfs(i,k,is_start):
            if k == 0: return 1 
            if i == n: return 0
            ans = dfs(i+1,k,is_start)
            if is_start:
                ans += dfs(i+1,k,False)
            else:
                ans += dfs(i,k-1,True)
            return ans%mod
        return dfs(0,k,True)%mod 