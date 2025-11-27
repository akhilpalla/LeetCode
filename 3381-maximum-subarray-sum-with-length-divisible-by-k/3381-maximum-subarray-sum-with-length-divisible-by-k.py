class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        dp = [-inf] * (len(nums)+1)
        for i in range(k, len(nums)+1):
            dp[i] = (prefix_sums[i] - prefix_sums[i-k]) + max(0, dp[i-k])
        return max(dp)