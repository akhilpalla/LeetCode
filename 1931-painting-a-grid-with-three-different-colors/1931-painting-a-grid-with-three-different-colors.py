class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        colors=[0,5,10]
        def next(prev,curr,j):
            A=[]
            for color in colors:
                if prev&(1<<(j+color))==0 and (j==0 or curr&(1<<(j+color-1))==0):
                    A.append(curr|1<<(j+color))
            return A

        mod=10**9+7
        @cache
        def solve(prev,curr,i,j):
            if i==n:
                return 1
            if j==m:return solve(curr,0,i+1,0)
            new=next(prev,curr,j)
            res=0
            if new:
                for final in new:
                    res+=solve(prev,final,i,j+1)
            return res%mod
        return solve(0,0,0,0)              