class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            #0 if edge is correctly oriented, 1 otherwise
            tree[u].append((v, 0))
            tree[v].append((u, 1))
        def dfs(u, p):
            return sum(d + dfs(v, u) for v, d in tree[u] if v != p)
        def dp(u, p, x):
            for v, d in tree[u]:
                if v == p:
                    continue
                ans[v] = x- 1 if d else x+1
                dp(v, u, ans[v])
        ans = [dfs(0, -1)] + [0] * (n-1)
        dp(0, -1, ans[0])
        return ans