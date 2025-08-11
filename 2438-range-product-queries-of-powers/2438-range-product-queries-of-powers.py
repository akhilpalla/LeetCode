class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        i = 0
        while (1 << i) <= n:
            if n & (1 << i):
                powers.append(1 << i)
            i += 1
        prefix_product = [1] * (len(powers) + 1)
        for i in range(1, len(powers) + 1):
            prefix_product[i] = (prefix_product[i - 1] * powers[i - 1]) % MOD
        result = []
        for l, r in queries:
            result.append((prefix_product[r + 1] * pow(prefix_product[l], MOD - 2, MOD)) % MOD)
        return result