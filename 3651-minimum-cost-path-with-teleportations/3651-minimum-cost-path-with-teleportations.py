class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        vdict = {}
        for i in range(M):
            for j in range(N):
                vdict.setdefault(grid[i][j], set()).add((i, j))
        vs = sorted(vdict.keys())[::-1]
        dp = [[inf for i in range(N)] for j in range(M)]
        dp[0][0] = 0
        for r in range(k+1):
            newdp = [[dp[i][j] for j in range(N)] for i in range(M)]
            minprev = inf
            if r > 0:
                for v in vs:
                    for di,dj in vdict[v]:
                        minprev = min(minprev,dp[di][dj])
                    for di,dj in vdict[v]:
                        newdp[di][dj] = minprev
            for i in range(M):
                for j in range(N):
                    v = grid[i][j]
                    if i - 1 >= 0:
                        newdp[i][j] = min(newdp[i][j],newdp[i-1][j]+v)
                    if j - 1 >= 0:
                        newdp[i][j] = min(newdp[i][j],newdp[i][j-1]+v)
            dp = [[newdp[i][j] for j in range(N)] for i in range(M) ]
        return dp[M-1][N-1]