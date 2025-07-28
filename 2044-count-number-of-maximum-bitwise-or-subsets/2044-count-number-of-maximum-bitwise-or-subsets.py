class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = 0
        for num in nums:
            maxor = maxor | num

        return self.helper(nums, 0, maxor, 0)

    def helper(self, nums: List[int], i: int, maxor: int, curxor: int) -> int:
        if curxor == maxor:
            remaining = len(nums) - i
            return 2 ** remaining

        if i == len(nums):
            return 0

        return self.helper(nums, i+1, maxor, curxor | nums[i]) + self.helper(nums, i+1, maxor, curxor)