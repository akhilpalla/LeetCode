class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dp(idx, rem):
            if idx == len(nums):
                if rem == 0:
                    return 0
                else:
                    return float("-inf")
            take = dp(idx + 1, (rem + nums[idx]) % 3) + nums[idx]
            skip = dp(idx+1, rem)
            return max(take, skip)
        return dp(0, 0)