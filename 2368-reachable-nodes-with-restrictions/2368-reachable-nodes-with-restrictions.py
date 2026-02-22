class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = [False]*n
        
        restricted = set(restricted)
        
        max_trav = 0
        
        graph = defaultdict(list)
        
        for x,y in edges:
            if x not in restricted and y not in restricted:
                graph[x].append(y)
                graph[y].append(x)
            
        def dfs(node):
            num_visit = 0
            if not seen[node]:
                num_visit = 1
                seen[node] = True
                
                for neighbor in graph[node]:
                    num_visit += dfs(neighbor)
                
            return num_visit
        
        return dfs(0)