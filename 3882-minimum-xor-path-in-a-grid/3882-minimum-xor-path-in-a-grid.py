class Solution:
    def minCost(self, g: list[list[int]]) -> int:
        return min((f:=cache(lambda i,j:set() if i//len(g)|j//len(g[0]) else 
            {g[i][j]^v for v in f(i+1,j)|f(i,j+1)} or {g[i][j]}))(0,0))