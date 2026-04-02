class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        g = defaultdict(list)
        for i in range(len(pid)):
            if ppid[i] == 0:
                continue
            g[ppid[i]].append(pid[i])
        q = deque([kill])
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nbr in g[curr]:
                q.append(nbr)
        return ans