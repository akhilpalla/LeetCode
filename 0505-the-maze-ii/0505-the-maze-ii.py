class Solution:
    def shortestDistance(self, grid, s, t):
        if grid[s[0]][s[1]] == 1:
            return -1
        n, m = len(grid), len(grid[0])
        q = collections.deque()
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        px = [0, 1, -1, 0]
        py = [1, 0, 0, -1]
        q.append((s[0], s[1]))
        dist[s[0]][s[1]] = 0   
        while q:
            p, r = q.popleft()
            for dx, dy in zip(px, py):
                roll = dist[p][r]
                x, y = p, r
                while 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    roll += 1
                if roll < dist[x][y]:
                    dist[x][y] = roll
                    q.append((x, y))
        if dist[t[0]][t[1]] == float('inf'):
            return -1
        return dist[t[0]][t[1]]
        if dist[t[0]][t[1]] == float('inf'):
            return -1
        return dist[t[0]][t[1]]