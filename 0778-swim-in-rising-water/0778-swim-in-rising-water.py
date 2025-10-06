class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        min_max = float('inf')

        visited = [[False]*n for _ in range(n)]
        @cache
        def dfs(i, j, current_max):
            nonlocal min_max
            if i < 0 or j < 0 or i >= n or j >= n or visited[i][j]:
                return
            current_max = max(current_max, grid[i][j])
            if current_max >= min_max:
                return  
            if i == n - 1 and j == n - 1:
                min_max = min(min_max, current_max)
                return
            visited[i][j] = True
            for dx, dy in directions:
                dfs(i + dx, j + dy, current_max)
            visited[i][j] = False

        dfs(0, 0, grid[0][0])
        return min_max