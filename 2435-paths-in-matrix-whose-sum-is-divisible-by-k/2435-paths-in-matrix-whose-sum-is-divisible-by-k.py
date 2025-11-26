class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = (10 ** 9) + 7
        
        memo = [[[-1 for _ in range(k)] for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def __recursion(sumi, r, c):
            nonlocal memo
            
            if (r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0])):
                return 0
            
            sumi += grid[r][c]

            if (r == len(grid) - 1 and 
                c == len(grid[0]) - 1):
                if sumi % k == 0:
                    return 1
                else:
                    return 0

            mod = sumi % k

            if memo[r][c][mod] != -1:
                return memo[r][c][mod]
            
            memo[r][c][mod] = __recursion(sumi, r + 1, c) + __recursion(sumi, r, c + 1)

            return memo[r][c][mod]
        
        return __recursion(0, 0, 0) % MOD