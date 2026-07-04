from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        visited = set()
        answer = float("inf")
        def dfs(city):
            nonlocal answer
            visited.add(city)
            for neighbor, dist in graph[city]:
                answer = min(answer, dist)
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(1)
        return answer