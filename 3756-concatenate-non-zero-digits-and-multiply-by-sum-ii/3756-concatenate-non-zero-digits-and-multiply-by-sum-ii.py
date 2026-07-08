class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9+7
        n = len(s)
        pow10 = [1] * (n + 1)
        num = [0]*(n+1)
        prefix = [0]*(n+1)
        length = [0]*(n+1)
        prev = 0
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % mod
        for i in range(n):
            curr = int(s[i])
            if curr > 0 :
                num[i+1] = (num[i]*10+curr)%mod
                prev = num[i+1]
                length[i+1] = length[i]+1
            else:
                if i > 0:
                    num[i+1] += num[i]
                    length[i+1] = length[i]
            prefix[i+1] = (prefix[i] if i > 0 else 0) + curr
        ans = []
        for l,r in queries:
            sums = prefix[r+1]-prefix[l]
            lent = length[r+1]-length[l]
            first = ((num[l])*pow10[lent])%mod
            last = num[r+1]
            nums = (last-first)%mod
            ans.append((nums*sums)%mod)
        return ans