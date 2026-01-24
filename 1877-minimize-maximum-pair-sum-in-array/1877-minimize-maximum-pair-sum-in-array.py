class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        half = n//2
        res = -float('inf')
        for i in range(half):
            pair_i = n-1 - i
            res = max(res, nums[i]+nums[pair_i])
        return res