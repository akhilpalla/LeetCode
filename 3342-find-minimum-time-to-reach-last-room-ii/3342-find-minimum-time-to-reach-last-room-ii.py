class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        DX = [0, 1, 0, -1]
        DY = [-1, 0, 1, 0]
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[ float(inf) for i in range(m)] for i in range(n)]
        vis = [[ 0 for i in range(m)] for i in range(n)]
        dist[0][0] = 0
        pq = []
        heappush(pq, [0, 0, 0, 1])  
        while pq:
            time, i, j, altTime = heappop(pq)
            if vis[i][j] == 1:
                continue
            vis[i][j] = 1
            for k in range(4):
                ii = DX[k] + i
                jj = DY[k] + j
                if 0 <= ii and ii < n and 0 <= jj and jj < m:
                    cost = altTime
                    if time < moveTime[ii][jj]:
                        cost += (moveTime[ii][jj] - time)
                    nextAltTime = 1 if altTime == 2 else 2
                    if dist[ii][jj] > dist[i][j] + cost:
                        dist[ii][jj] = dist[i][j] + cost
                        heappush(pq, [dist[ii][jj], ii, jj, nextAltTime])
        return dist[n-1][m-1]