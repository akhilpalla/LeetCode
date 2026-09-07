class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        last = [0] * 26

        total = 1
        ord_ = ord
        mod = MOD
        last_local = last
        s_local = s

        for k in range(len(s_local)):
            i = ord_(s_local[k]) - 97
            prev = total
            total = (total + total - last_local[i]) % mod
            last_local[i] = prev

        return (total - 1) % mod

