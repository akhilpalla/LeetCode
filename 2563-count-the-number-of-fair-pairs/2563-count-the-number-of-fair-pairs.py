class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:

        f = lambda x: sum(bisect_right(nums, x - num, hi = i)
                                      for i, num in enumerate(nums))
        nums.sort()

        return f(upper) - f(lower - 1)