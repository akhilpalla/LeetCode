class Solution:
    DWORD = 32
    MOD = 10 ** 9 + 7
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * Solution.DWORD
        for num in nums:
            for i in range(Solution.DWORD):
                if num & (1 << i) != 0:
                    bits[i] += 1
        res = 0
        for _ in range(k):
            x = 0
            for i in range(Solution.DWORD):
                if bits[i] > 0:
                    x += 1 << i
                    bits[i] -= 1
            res += x ** 2
            res %= Solution.MOD
        return res