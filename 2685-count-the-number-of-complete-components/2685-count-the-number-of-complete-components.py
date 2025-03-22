class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n

        def find(x): 
            while x != par[x]: 
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(n1, n2): 

            p1, p2 = find(n1), find(n2)
            if p1 == p2: 
                return

            if rank[p1] > rank[p2]: 
                rank[p1] += rank[p2]
                par[p2] = p1
            else: 
                rank[p2] += rank[p1] 
                par[p1] = p2

            return
        
        
        order = defaultdict(int)
        for a, b in edges: 
            union(a, b)
            order[a] += 1
            order[b] += 1
        
        complete_graph_tracker = defaultdict(int)
        for i in range(n):
            parent = find(i)
            num_of_nodes = rank[parent]
            if order[i] == num_of_nodes - 1: 
                complete_graph_tracker[parent] += 1
        
        ans = 0
        for key, value in complete_graph_tracker.items(): 
            if rank[key] == value: 
                ans += 1
        return ans
