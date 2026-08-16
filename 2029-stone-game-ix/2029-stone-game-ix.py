class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a,b,c=0,0,0
        for i in stones:
            r=i%3
            if r==0:
                a+=1
            elif r==1:
                b+=1
            else:
                c+=1
        if a%2==0:
            return b>0 and c>0
        return abs(b-c)>2        