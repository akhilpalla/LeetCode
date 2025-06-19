class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        def z_array(s):
            n = len(s)
            z = [0]
            l, r = 0, 0
            for i in range(1, n):
                z.append(min(r - i, z[i - l]) if i < r else 0)
                while i + z[i] < n and s[z[i]] == s[i+z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            return z      
        
        n, m, l = len(grid), len(grid[0]), len(pattern)
        h = "".join("".join(row) for row in grid)
        v = "".join(grid[i][j] for j in range(m) for i in range(n))

        h_match = z_array(pattern + '#' + h)[l + 1:]
        v_match = z_array(pattern + '#' + v)[l + 1:]
        
        for i, z in enumerate(h_match):
            if z < l:
                h_match[i] = h_match[i-1] - 1 if i and h_match[i-1] else 0
        for i, z in enumerate(v_match):
            if z < l:
                v_match[i] = v_match[i-1] - 1 if i and v_match[i-1] else 0
        ans = 0
        for i in range(n):
            for j in range(m):
                if h_match[i * m + j] and v_match[j * n + i]:
                    ans += 1
        return ans