class Solution:
    def idealArrays(self, m: int, n: int) -> int:
        def dec(num):
            i = 2
            ct = Counter()
            while i <= num//i:
                if num % i == 0:
                    j = 0
                    while num % i == 0:
                        num //= i
                        j += 1
                    ct[i] = j
                i += 1
            if num!=1:
                ct[num] += 1
            return ct
        mod = 10**9 + 7
        res = 1
        for i in range(2,n+1):
            ctr = dec(i)
            p = 1
            for key in ctr:
                ct = ctr[key]
                p = (p * comb(m+ct-1, m-1)) % mod
            res = (res + p) % mod
        return res