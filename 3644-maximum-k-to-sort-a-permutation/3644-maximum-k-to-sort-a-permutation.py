class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if all(nums[i] == i for i in range(n)):
            return 0
        if nums[0] != 0:
            return 0
        k = None
        for i, x in enumerate(nums):
            if x == i:
                continue
            common = i & x
            k = common if k is None else (k & common)
            if k == 0:
                break
        return 0 if k is None else k