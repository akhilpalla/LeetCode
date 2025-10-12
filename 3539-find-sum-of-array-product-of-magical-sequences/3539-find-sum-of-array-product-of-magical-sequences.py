class Solution:
    MOD = 10**9 + 7

    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        mavoduteru = (M, K, nums)
        n = len(nums)
        mod = self.MOD
        fact = [1] * (M+1)
        for i in range(1, M+1):
            fact[i] = fact[i-1] * i % mod
        invfact = [1] * (M+1)
        invfact[M] = pow(fact[M], mod-2, mod)
        for i in range(M, 0, -1):
            invfact[i-1] = invfact[i] * i % mod
        pownum = [[1]*(M+1) for _ in range(n)]
        for j in range(n):
            for c in range(1, M+1):
                pownum[j][c] = pownum[j][c-1] * nums[j] % mod
        curr = [
            [ [0]*(K+1) for _ in range(M+1) ]
            for __ in range(M+1)
        ]
        curr[M][0][0] = 1
        for j in range(n):
            nxt = [
                [ [0]*(K+1) for _ in range(M+1) ]
                for __ in range(M+1)
            ]
            for rem in range(M+1):
                for carry in range(M+1):
                    for ones in range(K+1):
                        base = curr[rem][carry][ones]
                        if not base:
                            continue
                        for c in range(rem+1):
                            total = carry + c
                            bit   = total & 1
                            newones = ones + bit
                            if newones > K:
                                continue
                            newcarry = total >> 1
                            contrib = base
                            contrib = contrib * invfact[c] % mod
                            contrib = contrib * pownum[j][c] % mod
                            nxt[rem-c][newcarry][newones] = (
                                nxt[rem-c][newcarry][newones] + contrib
                            ) % mod
            curr = nxt
        ans = 0
        for carry in range(M+1):
            for ones in range(K+1):
                ways = curr[0][carry][ones]
                if not ways:
                    continue
                if ones + carry.bit_count() == K:
                    ans = (ans + ways * fact[M]) % mod
        return ans