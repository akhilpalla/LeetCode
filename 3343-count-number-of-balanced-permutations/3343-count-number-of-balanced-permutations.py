class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        @cache
        def dfs(i, c1, c2, acc):
            if i > 10 or c1 > N1 or c2 > N2 or acc > total // 2:
                return 0   
            if c1 == N1 and c2 == N2:
                return 1 if acc == total // 2 else 0
            c = 0
            for k1 in range(C[i] + 1):
                n1, n2 = N1 - c1, N2 - c2
                k2 = C[i] - k1
                c += comb(n1, k1) * comb(n2, k2) * dfs(i + 1, c1 + k1, c2 + k2, acc + k1 * i)
                c %= M
            return c
        
        C, M = defaultdict(int), 10 ** 9 + 7
        N1, N2 = len(num) // 2, (len(num) + 1) // 2   
        total = 0
        for n in num:
            C[int(n)] += 1
            total += int(n)
        if total % 2 == 1:
            return 0
        return dfs(0, 0, 0, 0) % M