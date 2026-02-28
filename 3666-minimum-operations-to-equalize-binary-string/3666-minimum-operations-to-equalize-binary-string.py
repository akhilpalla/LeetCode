class Solution:
    def ceil_div(self,x, y):
        return (x + y - 1) // y
    def minOperations(self, S, K):
        N = len(S)
        Z = S.count('0')
        if N == K:
            return 0 if Z == 0 else 1 if Z == N else -1
        ans = float('inf')
        if Z % 2 == 0:
            M = max(self.ceil_div(Z, K), self.ceil_div(Z, N-K))
            if M % 2: M += 1
            ans = min(ans, M)
        if Z % 2 == K % 2:
            M = max(self.ceil_div(Z, K), self.ceil_div(N-Z, N-K))
            if M % 2 == 0: M += 1
            ans = min(ans, M)
        return ans if ans != float('inf') else -1