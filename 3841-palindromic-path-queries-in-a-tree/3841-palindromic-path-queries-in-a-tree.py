class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        LOG = n.bit_length()
        if LOG == 0: LOG = 1 
        par = [[-1] * n for _ in range(LOG)]
        dep = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        current_s_vals = [ord(c) - ord('a') for c in s]
        timer = 0
        def dfs(u, p):
            nonlocal timer
            tin[u] = timer
            timer += 1
            par[0][u] = p
            val = 1 << current_s_vals[u]
            pref[u] = (pref[p] if p != -1 else 0) ^ val
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)
            tout[u] = timer - 1
        dfs(0, -1)
        for k in range(1, LOG):
            for i in range(n):
                if par[k-1][i] != -1:
                    par[k][i] = par[k-1][par[k-1][i]]
        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u
            for k in range(LOG - 1, -1, -1):
                if par[k][u] != -1 and dep[par[k][u]] >= dep[v]:
                    u = par[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if par[k][u] != par[k][v]:
                    u = par[k][u]
                    v = par[k][v]
            return par[0][u]
        bit = [0] * (n + 1)
        def update_bit(i, x):
            i += 1   
            while i <= n:
                bit[i] ^= x
                i += i & -i
        def query_bit(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res
        ans = []
        for q in queries:
            parts = q.split()
            type_str = parts[0]
            if type_str[0] == 'u':  
                u = int(parts[1])
                c_char = parts[2]
                val_new = ord(c_char) - ord('a')
                val_old = current_s_vals[u]
                diff = (1 << val_old) ^ (1 << val_new)
                current_s_vals[u] = val_new   
                update_bit(tin[u], diff)
                update_bit(tout[u] + 1, diff)
            else:   
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                curr_pref_u = pref[u] ^ query_bit(tin[u])
                curr_pref_v = pref[v] ^ query_bit(tin[v])
                val_w = 1 << current_s_vals[w]
                mask = curr_pref_u ^ curr_pref_v ^ val_w
                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans