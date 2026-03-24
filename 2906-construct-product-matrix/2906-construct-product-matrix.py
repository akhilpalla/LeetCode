class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        m=len(g)
        n=len(g[0])
        pr=[3, 5, 823]
        f=[]
        d=[0]*3
        for k in range(3):
            p=pr[k]
            tmp=0
            for i in range(m):
                gr=g[i]
                for j in range(n):
                    if gr[j]%p==0:
                        tmp+=1
                    if tmp==1 and d[k]==0:
                        d[k]=(i, j)
                    if tmp>=2:
                        break
            f.append(tmp)
        dct=[0]*3
        for k in range(3):
            if f[k]==0:
                prod=1
                p=pr[k]
                for i in range(m):
                    gr=g[i]
                    for j in range(n):
                        prod=prod*gr[j]%p
                dct[k]=prod
            elif f[k]==1:
                prod=1
                p=pr[k]
                i0, j0=d[k]
                for i in range(m):
                    gr=g[i]
                    for j in range(n):
                        if (i, j)!=(i0, j0):
                            prod=prod*gr[j]%p
                dct[k]=prod
        
        v1=-5*823
        v2=-3*823
        v3=8*823+1
        tmp=[0, 0, 0]
        for i in range(m):
            gr=g[i]
            for j in range(n):                
                for k in range(3):
                    if f[k]==0:
                        tmp[k]=dct[k]*pow(gr[j], -1, pr[k])%pr[k]
                    elif f[k]==1:
                        tmp[k]=dct[k] if (i, j)==d[k] else 0
                    else:
                        tmp[k]=0
                gr[j]=(v1*tmp[0]+v2*tmp[1]+v3*tmp[2])%12345
        return g
        