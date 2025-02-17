class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        n = len(nums)
        res = 0
        count = {}
        while j < n:
            count[nums[j]] = count.get(nums[j], 0) + 1
            while count[nums[j]] > k:
                count[nums[i]] = count.get(nums[i], 0) - 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res