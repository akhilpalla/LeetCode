class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i:[] for i in range(n) }
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neigh in adj[node]:
                if neigh not in visit:
                    dfs(neigh)
        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        return count