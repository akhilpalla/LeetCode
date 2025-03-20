from collections import defaultdict
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def fin_par(a):
            if a==par[a]:
                return a
            par[a] =fin_par(par[a])
            return par[a]  
        def union(u,v):
            a=fin_par(u)
            b=fin_par(v)
            if rank[u]>rank[v]:
                par[b]=a
            elif rank[u]<rank[v]:
                par[a]=b
            else:
                rank[b]+=1
                par[a]=b

                         
        par={i:i for i in range(n)}
        rank=[0]*n
        for u,v,w in edges:
            union(u,v)
        dic=defaultdict(int)    
        for u,v,w in edges:
            a=fin_par(u)
            b=fin_par(v)
            if a==b:
                if a not in dic:
                    dic[a]=w
                else:    
                    dic[a]&=w
        ans=[]
        for u,v in query:
            if u==v:
                ans.append(0)
            else:    
                a=fin_par(u)
                b=fin_par(v)
                if a==b:
                    ans.append(dic[a])
                else:
                    ans.append(-1)
        return ans                        