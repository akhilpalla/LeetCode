class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
        
    def find(self, v):
        if v != self.p[v]:
            self.p[v] = self.find(self.p[v])
        return self.p[v]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v) -> bool:
        up, vp = self.find(u), self.find(v)
        if up == vp:
            return False
        
        if self.r[up] > self.r[vp]:
            self.p[vp] = up
        elif self.r[up] < self.r[vp]:
            self.p[up] = vp
        else:
            self.p[up] = vp
            self.r[vp] += 1
            
        return True
        

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n+1) # ignoring 0 since it is not in the graph
        connections.sort(key=lambda x:x[2])
        mst = cost = 0
        for u, v, w in connections:
            if uf.connected(u, v):
                continue
            uf.union(u, v)
            mst += 1
            cost += w
            if mst == n - 1:
                return cost
        
        return -1