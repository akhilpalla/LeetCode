class Solution:
    def distributeCandies(self, n: int, l: int) -> int:
        if 3*l < n:return 0
        res = (n+1)*(n+2) // 2
        
        n -= l + 1
        if n >= 0:
            res -= 3*(n+1)*(n+2) // 2
        n -= l + 1
        if n >= 0:
            res += 3*(n+1)*(n+2) // 2

        return res