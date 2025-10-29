class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i == n: return 0
            res = float('inf')
            for j in range(i,n):
                if gcd(nums[i],nums[j]) > 1:
                    res = min(res, 1+dfs(j+1))
            return res
        opt = dfs(0)
        return -1 if opt == float('inf') else opt