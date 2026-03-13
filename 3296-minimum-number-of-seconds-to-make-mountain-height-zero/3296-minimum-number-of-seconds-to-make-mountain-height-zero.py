class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        heap = []
        for worker, initial_time in enumerate(workerTimes):
            heappush(heap, (initial_time, worker, 1))
        while mountainHeight:
            mountainHeight -= 1
            end_time, worker, height = heappop(heap)
            heappush(heap, (end_time + workerTimes[worker] * (height + 1), worker, height + 1))

        return end_time