class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def getStartPos():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "*":
                        return (i, j)
                    
        startX, startY = getStartPos()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False for c in range(n)] for r in range(m)]
        visited[startX][startY] = True
        q = collections.deque([(0, startX, startY)])
        
        while q:
            steps, x, y = q.popleft()
            
            if grid[x][y] == "#":
                return steps
            
            for dX, dY in dirs:
                nX, nY = x + dX, y + dY
                
                if m > nX >= 0 <= nY < n and grid[nX][nY] != "X" and not visited[nX][nY]:
                    visited[nX][nY] = True
                    q.append((steps+1, nX, nY))
        
        return -1
		