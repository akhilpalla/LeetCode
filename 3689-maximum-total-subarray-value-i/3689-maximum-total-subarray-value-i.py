class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        minval, maxval = min(nums), max(nums)
        return k * (maxval - minval)