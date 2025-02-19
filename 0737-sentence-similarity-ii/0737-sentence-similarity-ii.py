class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        m, n = len(sentence1), len(sentence2)
        if m != n:
            return False

        uf = UnionFind()
        for a, b in similarPairs:
            uf.add(a)
            uf.add(b)
            uf.union(a, b)
        
        for a, b in zip(sentence1, sentence2):
            if a != b:
                if a not in uf.root or b not in uf.root:
                    return False
                elif uf.find(a) != uf.find(b):
                    return False
        return True

class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = {}
    
    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 1
        return
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1