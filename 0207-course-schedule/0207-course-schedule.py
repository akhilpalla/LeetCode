#We can use TopoSort using Khan;s Algo or DFS cycle detection using path visited and visited (if there is a cycle we cant have topo sort so order not possible)
"""
# Using Topo Sort

class Solution:

    def bfs(self, inDeg, adj, V):
        ans = []
        q = deque()
        for i in range(V):
            if inDeg[i] == 0:
                q.append(i)
        
        while len(q) != 0:
            node = q.popleft()
            ans.append(node)
            for neigh in adj[node]:
                inDeg[neigh] -= 1
                if inDeg[neigh] == 0:
                    q.append(neigh)
        
        return ans

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses #just to fit old code
        adj = [[] for _ in range(n)]
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
        
        inDeg = [0] * n
        
        for nodes in adj:
            for neighs in nodes:
                inDeg[neighs] += 1
        
        ans = self.bfs(inDeg, adj, n)
        
        if len(ans) < n:
            return False
        else:
            return True

#instead of storing the actual topo sort we can just keep counter also 
# T = V+E
# S = V
"""

from collections import deque

class Solution:
    def dfs(self, node, adj, vis, pVis):
        vis[node] = 1
        pVis[node] = 1
        
        for neigh in adj[node]:
            if vis[neigh] == 0:
                if self.dfs(neigh, adj, vis, pVis) == True:
                    return True
            elif pVis[neigh] == 1:
                return True
        
        pVis[node] = 0
        return False



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses #just to fit old code
        adj = [[] for _ in range(n)]
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
        vis = [0]*n
        pVis = [0]*n
        for i in range(n):
            if vis[i] == 0:
                if self.dfs(i, adj, vis, pVis) == True:
                    return False
        return True

# T = V + E
# S = 2N + N