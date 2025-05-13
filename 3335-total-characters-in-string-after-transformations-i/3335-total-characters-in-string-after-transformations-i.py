class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cn = Counter(s)
        memo = {}
        def rec(n):
            if n in memo:
                return memo[n]
            if n < 26:
                return 1
            cnt = 0
            cnt += rec(n - 26) + rec(n - 25)
            memo[n] = cnt
            return memo[n]
        cnt = 0
        for st in cn:
            cnt += cn[st] * rec(t + (ord(st) - 97))
        return cnt % ((10 ** 9) + 7)