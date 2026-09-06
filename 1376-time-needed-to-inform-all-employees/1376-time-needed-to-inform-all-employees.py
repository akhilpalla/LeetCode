from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                adj[mgr].append(emp)
        res = 0
        q = deque([(headID, informTime[headID])])
        while q:
            mgr, t = q.popleft()
            res = max(res, t)
            for ch in adj[mgr]:
                q.append((ch, t + informTime[ch]))
        return res