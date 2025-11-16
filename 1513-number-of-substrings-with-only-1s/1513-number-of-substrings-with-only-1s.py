class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        cnt = 0
        for i in s.split('0'):
            n = len(i)
            cnt += n*(n + 1)
        return (cnt // 2) % mod