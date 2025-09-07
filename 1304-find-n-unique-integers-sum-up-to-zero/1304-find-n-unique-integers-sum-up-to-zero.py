class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1: return [0]
        if n == 2: return [-1, 1]
        l = list(range(n-1))
        l.append(-sum(l))
        return l