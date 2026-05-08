class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        mx = max(nums)
        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        mp = {}
        for i, val in enumerate(nums):
            x = val
            used = set()
            while x > 1:
                p = spf[x]
                if p not in used:
                    if p not in mp:
                        mp[p] = []
                    mp[p].append(i)
                    used.add(p)
                x //= p
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0
        while q:
            i = q.popleft()
            steps = dist[i]
            if i == n - 1:
                return steps
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = steps + 1
                q.append(i - 1)
            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = steps + 1
                q.append(i + 1)
            val = nums[i]
            if val > 1 and spf[val] == val:
                for nxt in mp.get(val, []):
                    if dist[nxt] == -1:
                        dist[nxt] = steps + 1
                        q.append(nxt)
                mp[val] = []
        return -1