class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        @cache
        def maxFruits(i, j, steps):
            if i == n-1 and j == n-1:
                return 0
            if steps == 0:
                return -math.inf
            ans = 0
            for d1, d2 in dirs:
                x = i + d1
                y = j + d2
                if 0 <= x < n and 0 <= y < n:
                    ans = max(ans, grid[x][y] + maxFruits(x, y, steps-1))
            return ans
        
        n = len(fruits)
        res = sum([fruits[i][i] for i in range(n)])
        
        dirs = [[1, -1], [1, 0], [1, 1]]
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                grid[i][j] = fruits[i][j]
        res += fruits[0][n-1] + maxFruits(0, n-1, n-1)

        dirs = [[-1, 1], [0, 1], [1, 1]]
        grid = [[0 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for i in range(j+1, n):
                grid[i][j] = fruits[i][j]
        res += fruits[n-1][0] + maxFruits(n-1, 0, n-1)

        return res



        