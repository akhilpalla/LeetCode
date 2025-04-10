class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suf = int(s)
        if finish < suf:
            return 0
        inc = 10 ** len(s)
        def cnt(x):
            ans = 0 if x % inc < suf else 1
            x //= inc
            digitValue = 1
            while x:
                d = x % 10
                x //= 10
                if d > limit:  
                    ans = (limit + 1) * digitValue
                else:
                    ans += d * digitValue
                digitValue *= limit + 1
            return ans
        return cnt(finish) - cnt(start - 1)