class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
        visited, path = set(), set()
        n = len(colors)
        count = [[0] * 26 for i in range(n)]
        def dfs(node):
            if node in path:
                return inf
            if node in visited:
                return 0
            visited.add(node)
            path.add(node)
            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] += 1
            for adj in g[node]:
                if dfs(adj) == inf:
                    return inf
                for i in range(26):
                    count[node][i] = max(count[node][i], count[adj][i] + (1 if colorIndex == i else 0))
            path.remove(node)
            return max(count[node])
        res = 0
        for i in range(n):
            if i not in visited:
                res = max(res, dfs(i))
        return res if res != inf else -1