class Solution:
    def __init__(self):
        coors = [(x, y) for x in range(3) for y in range(3)]
        self.neighbors: List[List[int]] = [[] for _ in range(9)]
        self.over_center: List[List[Tuple[int, int]]] = [[] for _ in range(9)]

        for i in range(1, 9):
            x1, y1 = coors[i]
            for j in range(i):
                x2, y2 = coors[j]
                dy, dx = abs(y2 - y1), abs(x2 - x1)
                k1 = y1 * 3 + x1
                k2 = y2 * 3 + x2
                if (dy == dx or dy == 0 or dx == 0) and (dy == 2 or dx == 2):
                    mid = ((y1 + y2) // 2) * 3 + (x1 + x2) // 2
                    self.over_center[k1].append((k2, mid))
                    self.over_center[k2].append((k1, mid))
                else:
                    self.neighbors[k1].append(k2)
                    self.neighbors[k2].append(k1)

    def numberOfPatterns(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(v: int, length: int, mask: int) -> int:
            if length == 0:
                return 0
            if length == 1:
                return 1
            total = 0
            mask |= 1 << v

            for u in self.neighbors[v]:
                if not (mask >> u) & 1:
                    total += dfs(u, length - 1, mask)
            for u, mid in self.over_center[v]:
                if not (mask >> u) & 1 and (mask >> mid) & 1:
                    total += dfs(u, length - 1, mask)
            return total

        res = 0
        for L in range(m, n + 1):
            res += 4 * dfs(0, L, 0) + 4 * dfs(1, L, 0) + dfs(4, L, 0)
        return res