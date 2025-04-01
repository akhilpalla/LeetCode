class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        dists = collections.defaultdict(int)
        can_reach = collections.defaultdict(set)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(row, col):
            q = collections.deque([])
            q.append((row, col, 0))
            seen = set()
            seen.add((row, col))
            while q:
                r, c, d = q.popleft()
                dists[(r, c)] += d
                for y, x in dirs:
                    nr = r + y
                    nc = c + x
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        can_reach[(nr, nc)].add((row, col))
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1))
                        
        bs = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)
                    bs.add((row, col))
                    dists[(row, col)] = float('inf')
                    

        min_dist = float('inf')

        for k in dists:
            if dists[k] < min_dist and len(can_reach[k]) == len(bs):
                min_dist = dists[k]
        
        return min_dist if min_dist != float('inf') else -1