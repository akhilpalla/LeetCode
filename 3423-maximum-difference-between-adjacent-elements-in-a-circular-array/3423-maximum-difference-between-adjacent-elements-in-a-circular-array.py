class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        res = []
        for i in range(1,len(nums)):
            res.append(abs(nums[i-1]-nums[i]))
        return max(res)