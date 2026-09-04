class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        mn = nums[n-1]
        for i in range(n-1,-1,-1):
            mn=min(mn,nums[i])
            dp[i]=mn
        mx = nums[0]
        for i in range(n):
            mx=max(mx,nums[i])
            if k>=(mx-dp[i]):
                return i
        return -1