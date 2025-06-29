class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        f = [1] + [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            f[i] = f[i - 1] * 2 % MOD
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if nums[i] * 2 > target:
                break
            maxValue = target - nums[i]
            pos = bisect.bisect_right(nums, maxValue) - 1
            ans += f[pos - i] if pos >= i else 0
        return ans % MOD