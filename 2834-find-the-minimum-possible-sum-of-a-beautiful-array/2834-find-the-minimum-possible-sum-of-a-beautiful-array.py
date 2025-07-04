class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        h = target // 2
        if n <= h:
            return ((1 + n) * n // 2) % (10**9 + 7)
            
        left_sum = (1 + h) * h // 2
        right_sum = (2 * target + n - h - 1) * (n - h) // 2
        return (left_sum + right_sum) % (10**9 + 7)