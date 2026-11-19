class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[-1] - nums[2]
        ans = min(ans, nums[-3] - nums[0])
        ans = min(ans, nums[-2] - nums[1])
        return ans