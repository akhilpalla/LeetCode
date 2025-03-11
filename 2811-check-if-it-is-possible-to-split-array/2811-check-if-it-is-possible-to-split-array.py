class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        for i in range(1, n):
            total = nums[i-1] + nums[i]
            if total >= m:
                return True
        return False
        