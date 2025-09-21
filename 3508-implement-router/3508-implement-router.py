from collections import defaultdict, deque
import heapq, bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.space = deque()
        self.size = memoryLimit
        self.logs = defaultdict(list)   
        self.inSpace = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.inSpace:  
            return False

        if len(self.space) >= self.size:
            old_src, old_dest, old_time = self.space.popleft()
            self.inSpace.remove((old_src, old_dest, old_time))
            idx = bisect.bisect_left(self.logs[old_dest], old_time)
            self.logs[old_dest].pop(idx)

        self.space.append(packet)
        self.inSpace.add(packet)
        bisect.insort(self.logs[destination], timestamp)  
        return True

    def forwardPacket(self) -> list[int]:
        if not self.space:
            return []
        src, dest, ts = self.space.popleft()
        self.inSpace.remove((src, dest, ts))
        idx = bisect.bisect_left(self.logs[dest], ts)
        self.logs[dest].pop(idx)
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.logs[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left