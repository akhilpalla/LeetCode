class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        queue = deque()
        queue.append(startTime[0] - 0)
        for i in range(1,len(startTime)):
            queue.append(startTime[i] - endTime[i - 1])
        queue.append(eventTime - endTime[-1])
        mx = 0
        ind = 0
        for i in range(len(queue)):
            if queue[i] > mx:
                mx = queue[i]
                ind = i
        l = 0
        r = k + 1
        sm = 0
        for i in range(k + 1):
            sm += queue[i]
        mx = max(mx, sm)
        for i in range(k + 1, len(queue)):
            sm -= queue[l]
            l += 1
            sm += queue[i]
            mx = max(mx, sm)
        return mx