class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return 0
        score = float('inf')
        i = 0
        nums.sort()
        while k - 1 < n:
            score = min(score, nums[k - 1] - nums[i])
            i += 1
            k += 1
        return score