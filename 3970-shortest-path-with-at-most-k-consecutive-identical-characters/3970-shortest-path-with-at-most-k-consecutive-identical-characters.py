import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if not n-1: return 0
        graph=[[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
        inf=10**18; pq=[]
        dist=[[inf]*(k+1) for _ in range(n)]
        for v,w in graph[0]:
            c = 1 if labels[0]!=labels[v] else 2
            if c<=k: heapq.heappush(pq,(w,v,c))
        while pq:
            w,u,c=heapq.heappop(pq)
            # athere, c<=k always
            if u==n-1: return w
            elif w<dist[u][c]:
                dist[u][c]=w
                for v,d in graph[u]:
                    cnew= 1 if labels[u]!=labels[v] else c+1
                    dnew=d+w
                    if cnew>k: continue
                    for i in range(cnew+1):
                        if dist[v][i]<=dnew:
                            dnew=inf
                            break
                    if dist[v][cnew]>dnew:
                        heapq.heappush(pq,(dnew,v,cnew))
        return -1