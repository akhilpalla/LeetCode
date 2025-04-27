class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+2] == nums[i+1]/2:
                result += 1
        return result