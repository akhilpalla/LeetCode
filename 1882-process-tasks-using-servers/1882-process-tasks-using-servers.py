class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        server_avail = [(w,i) for i,w in enumerate(servers)]
        heapify(server_avail)
        tasks_in_progress = []
        res = []
        st=0
        for j,task in enumerate(tasks):
            st = max(st,j)
            if not server_avail:
                st = tasks_in_progress[0][0]
            while tasks_in_progress and tasks_in_progress[0][0]<=st:
                heapq.heappush(server_avail,heappop(tasks_in_progress)[1])
            res.append(server_avail[0][1])
            heapq.heappush(tasks_in_progress,(st+task,heappop(server_avail)))
        return res