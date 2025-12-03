class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        dct={}
        dct2={}
        l=len(points)
        for i in range(l):
            x1, y1=points[i]
            for j in range(i+1, l):
                x2, y2=points[j]
                m1=x1+x2
                m2=y1+y2
                if x1==x2:
                    slope=(1, 0)
                    intercept=x1
                else:
                    d1=y2-y1
                    d2=x2-x1
                    g=gcd(d1, d2)
                    d1//=g
                    d2//=g
                    if d2<0:
                        d1, d2=-d1, -d2
                    slope=(d1, d2)    
                    intercept=d2*y1-d1*x1
                if slope not in dct:
                    dct[slope]=defaultdict(set)
                dct[slope][intercept].add(tuple(points[i]))
                dct[slope][intercept].add(tuple(points[j]))
                if (m1, m2) not in dct2:
                    dct2[m1, m2]=defaultdict(int)
                dct2[m1, m2][slope]+=1
        ans=0
        for ls in dct.values():
            if len(ls)>1:
                sm=0
                sm2=0
                for v in ls.values():
                    l1=len(v)
                    t1=l1*(l1-1)//2
                    sm+=t1
                    sm2+=t1*t1
                ans+=sm*sm-sm2
        for val in dct2.values():
            if len(val)>1:
                sm=0
                sm2=0
                for v2 in val.values():
                    sm+=v2
                    sm2+=v2*v2
                ans-=sm*sm-sm2
        
        return ans>>1