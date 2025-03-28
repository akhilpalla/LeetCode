class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_first_idx = {0: -1}
        res = total = 0
        for i, num in enumerate(nums):
            total += 1 if num == 1 else -1
            if total in sum_first_idx:
                res = max(res, i - sum_first_idx[total])
            else:
                sum_first_idx[total] = i
        return res