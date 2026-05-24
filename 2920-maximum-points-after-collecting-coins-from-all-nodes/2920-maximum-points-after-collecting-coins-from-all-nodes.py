from collections import defaultdict
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        adj=defaultdict(list)
        if k==0:
            return sum(coins)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp=defaultdict(int)
        @cache
        def rec(nod,decay,k,par):
            if decay>=14:
                return 0
            ans=0
            t1=(coins[nod]>>decay)-k
            t2=(coins[nod]>>decay)//2
            for i in adj[nod]:
                if i !=par:
                    t1+=rec(i,decay,k,nod)
                    t2+=rec(i,decay+1,k,nod)
            return max(t1,t2)      
        return rec(0,0,k,-1)            