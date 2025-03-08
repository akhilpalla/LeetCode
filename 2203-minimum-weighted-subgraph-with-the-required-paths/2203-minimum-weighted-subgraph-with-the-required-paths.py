def dijk(s,g,n):
    dis=[float("inf")]*n
    par=[-1]*n
    dis[s]=0
    q=[(0,s)]
    while q:
        wt,t=heapq.heappop(q)
        if wt!=dis[t]:
            continue
        for i,w in g[t]:
            if w+wt<dis[i]:
                dis[i]=w+wt
                heapq.heappush(q,(w+wt,i))
                par[i]=t
    return dis,par
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        g=defaultdict(list)
        gr=defaultdict(list)
        for x,y,w in edges:
            g[x].append((y,w))
            gr[y].append((x,w))
        d1,p1=dijk(src1,g,n)
        d2,p2=dijk(src2,g,n)
        ans=float("inf")
        for i,w in gr[dest]:
            ans=min(ans,d1[i]+d2[i]+w,d1[dest]+d2[i]+w)
        ed=dest
        while ed!=-1:
            ans=min(ans,d1[dest]+d2[ed])
            ed=p1[ed]
        ed=dest
        while ed!=-1:
            ans=min(ans,d2[dest]+d1[ed])
            ed=p2[ed]
        ans=min(ans,d1[dest]+d2[dest])
        if ans==float("inf"):
            ans=-1
        return ans