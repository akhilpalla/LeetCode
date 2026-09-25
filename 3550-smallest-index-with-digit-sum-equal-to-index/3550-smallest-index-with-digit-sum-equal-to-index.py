class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def calc_digit_sum(num: int) -> int:
            total_sum = 0
            while num > 0:
                num, rem = divmod(num, 10)
                total_sum += rem
            return total_sum
        for idx, num in enumerate(nums):
            if idx == calc_digit_sum(num):
                return idx
        return -1