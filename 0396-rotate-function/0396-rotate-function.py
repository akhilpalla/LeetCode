class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        accumulation = 0
        for i, v in enumerate(nums):
            accumulation += i * v
            prefix_sums[i + 1] = prefix_sums[i] + v
        return accumulation + max(n * prefix_sums[k] - k * prefix_sums[n] for k in range(n))