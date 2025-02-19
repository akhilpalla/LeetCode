class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        x, y = moves[0]
        i, j = 0, 0
        
        for num in range(n*n):
            res[i][j] = num+1
            visited.add((i,j))
            if i+x == n or i+x == -1 or j+y == n or j+y == -1 or (i+x,j+y) in visited:
                moves.append(moves.pop(0))
            x, y = moves[0]
            i, j = i+x, j+y

        return res