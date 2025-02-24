class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        graph = defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(target):
            stack, visited = [[bob,[bob]]], set([bob])

            while stack:
                nd,path = stack.pop()

                if nd == 0:
                    return path

                for neighbor in graph[nd]:
                    if neighbor not in visited:
                        stack.append([neighbor,path+[neighbor]])
                        visited.add(neighbor)

        result = dfs(0)

        m = len(result)

        for i in range(m//2):
            amount[result[i]] = 0 

        if m%2 == 1: amount[result[m//2]] //= 2

        def bfs(node,parent):
            if len(graph[node]) == 1 and graph[node][0] == parent:
                return amount[node]

            max_val = float("-inf")

            for neighbor in graph[node]:
                if neighbor != parent:
                    max_val = max(max_val,bfs(neighbor,node))

            return amount[node] + max_val 

        return bfs(0,-1)