class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.map = {}
        self.h = []
        for userId, taskId, priorityId in tasks:
            self.map[taskId] = (userId, priorityId)
            self.h.append((-priorityId, -taskId, userId))
        heapq.heapify(self.h)

        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.map[taskId] = (userId, priority)
        heapq.heappush(self.h, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.map[taskId]
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        del(self.map[taskId])
        

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heapq.heappop(self.h)
            if -taskId not in self.map:
                continue
            
            userId, newPriority = self.map[-taskId]
            if newPriority != -priority:
                heapq.heappush(self.h, (-newPriority, taskId, userId))
                continue
            
            del self.map[-taskId]
            
            return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()