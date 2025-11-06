class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        class DisjointSet:
            def __init__(self,n):
                self.root = [i for i in range(n)]
                self.active = [True for i in range(n)]
                self.hm = None
            def set_false(self,n):
                self.active[n] = False
            def find(self,x):
                if self.root[x]!=x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            def union(self,x,y):
                X,Y = self.find(x),self.find(y)
                if X == Y:
                    return
                if X<Y:
                    self.root[Y] = X
                else:
                    self.root[X] = Y
            def compute(self,n):
                if self.active[n]:
                    return n+1
                else:
                    p = self.find(n)
                    if not self.hm[p]:
                        return -1
                    
                    while self.hm[p]:
                        top = self.hm[p][0]
                        if self.active[top]:
                            return top+1
                        else:
                            heapq.heappop(self.hm[p])
                    return -1
            def sync(self):
                n = len(self.root)
                hm = defaultdict(list)
                for i in range(n):
                    parent = self.find(i)
                    hm[parent].append(i)
                for k,v in hm.items():
                    heapq.heapify(v)
                self.hm = hm
                
        ds = DisjointSet(c)
        ans = []
        for u,v in connections:
            ds.union(u-1,v-1)
        ds.sync()
        for o,n in queries:
            if o == 2:
                ds.set_false(n-1)
            if o == 1:
                ans.append(ds.compute(n-1))
        return ans