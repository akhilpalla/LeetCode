class Solution:
    def maxProduct(self, n: int) -> int:
        st = sorted([int(i) for i in str(n)])
        return st[-1] * st[-2]