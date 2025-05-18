class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        
        pref_r = [[0] * (N + 1) for _ in range(M + 1)]
        pref_c = [[0] * (N + 1) for _ in range(M + 1)]


        for i in range(M):
            for j in range(N):
                pref_r[i][j + 1] += pref_r[i][j]
                if grid[i][j] == "W":
                    pref_r[i][j + 1] = 0
                if grid[i][j] == "E":
                    pref_r[i][j + 1] += 1
        
        for i in range(M):
            for j in range(N - 1, -1, -1):
                if j + 2 < N + 1 and grid[i][j] != "W":
                    pref_r[i][j + 1] = max(pref_r[i][j + 1], pref_r[i][j + 2])


        for j in range(N):
            for i in range(M):
                pref_c[i + 1][j] += pref_c[i][j]
                if grid[i][j] == "W":
                    pref_c[i + 1][j] = 0
                if grid[i][j] == "E":
                    pref_c[i + 1][j] += 1
        
        for j in range(N):
            for i in range(M - 1, -1, -1):    
                if i + 2 < M + 1 and grid[i][j] != "W":
                    pref_c[i + 1][j] = max(pref_c[i + 1][j], pref_c[i + 2][j])
        
        best = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "0":
                    best = max(best, pref_r[i][j + 1] + pref_c[i + 1][j])



        return best
