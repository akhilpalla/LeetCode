class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        def update(cur):
            if res[cur] == -1 and res[edges[cur]] != -1:
                res[cur] = 1 + res[edges[cur]]
                return True
            return False

        def dfs(cur):
            if cur in path_set:  
                s = path_list.index(cur)
                length = len(path_list) - s
                for node in path_list[s:]:
                    res[node] = length
            else:  
                path_list.append(cur)  
                path_set.add(cur)  
                if not update(cur):
                    dfs(edges[cur])
                    update(cur)
        
        n = len(edges)
        res = [-1]*n
        for i in range(n):
            if res[i] == -1:  
                path_list, path_set = list(), set()
                dfs(i)
                
        return res