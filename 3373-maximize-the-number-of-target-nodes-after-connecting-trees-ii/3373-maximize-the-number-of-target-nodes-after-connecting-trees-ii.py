class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def dfs(adj, node, prev, cols, counts):
            counts[cols[node]] += 1
            for ne in adj[node]:
                if ne != prev:
                    cols[ne] = 1 - cols[node]
                    dfs(adj, ne, node, cols, counts)
        
        tree1, tree2 = build(edges1), build(edges2)
        tree1Cols, tree2Cols = [0] * len(tree1), [0] * len(tree2)  
        tree1Counts, tree2Counts = [0,0], [0,0]  

        dfs(tree1, 0, None, tree1Cols, tree1Counts)
        dfs(tree2, 0, None, tree2Cols, tree2Counts)

        M = max(tree2Counts)

        ans = [0] * len(tree1)
        for i in range(len(ans)):
            ans[i] = tree1Counts[tree1Cols[i]] + M
        return ans
        
        