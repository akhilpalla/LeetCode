class Solution:
    def minOperations(self, queries):
        groups = []
        i = 1
        lo = 1
        while lo <= 10**9:
            hi = 4**i - 1
            if hi > 10**9:
                hi = 10**9
            groups.append((lo, hi, i))
            i += 1
            lo = 4**(i-1)
        def f(x):
            if x <= 0:
                return 0
            total = 0
            for lo, hi, op in groups:
                if x < lo:
                    break
                if x >= hi:
                    total += op * (hi - lo + 1)
                else:
                    total += op * (x - lo + 1)
                    break
            return total
        res = 0
        for l, r in queries:
            total_work = f(r) - f(l - 1)
            res += (total_work + 1) // 2
        return res