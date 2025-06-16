class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_val, max_diff = nums[-1], -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_val:
                max_diff = max(max_diff, max_val - nums[i])
            max_val = max(max_val, nums[i])
        return max_diff