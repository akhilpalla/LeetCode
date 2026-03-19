class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        lastCountX = {}
        lastCountY = {}

        ans = 0

        for i in range(col):
            lastCountX[i] = 0
            lastCountY[i] = 0


        for i in range(row):
            x = 0
            y = 0
            for j in range(col):
                if grid[i][j] == "X":
                    x += 1
                elif grid[i][j] == "Y":
                    y += 1
                
                
                currValueX = x + lastCountX[j]
                currValueY = y + lastCountY[j]
                
                if currValueX == currValueY and currValueX > 0:
                    ans += 1
                
                lastCountX[j] += x
                lastCountY[j] += y
        
        return ans