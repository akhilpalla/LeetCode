class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for num in nums:
            if num:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res