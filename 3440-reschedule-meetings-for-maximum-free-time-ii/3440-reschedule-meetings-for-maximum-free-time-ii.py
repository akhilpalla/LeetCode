from bisect import bisect_left

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        gaps = [0]*(n+1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i-1]
        gaps[n] = eventTime - endTime[-1]
        sortedGaps = sorted(gaps)
        durations = [endTime[i] - startTime[i] for i in range(n)]
        gapsWithIdx = sorted([(gaps[i], i) for i in range(n+1)], reverse=True)[:4]

        def pick(ex0, ex1):
            for val, idx in gapsWithIdx:
                if idx != ex0 and idx != ex1:
                    return val
            return 0

        def second(mv, ex0, ex1):
            c = []
            for val, idx in gapsWithIdx:
                if idx != ex0 and idx != ex1:
                    c.append(val)
                    if len(c) == 2:
                        break
            c.append(mv)
            c.sort(reverse=True)
            return c[1]

        best = sortedGaps[-1]
        for i in range(n):
            d = durations[i]
            merged = gaps[i] + d + gaps[i+1]
            cnt = n+1 - bisect_left(sortedGaps, d)
            if gaps[i] >= d:
                cnt -= 1
            if gaps[i+1] >= d:
                cnt -= 1
            if merged >= d:
                cnt += 1
            if cnt == 0:
                continue
            largest = max(merged, pick(i, i+1))
            if cnt >= 2:
                best = max(best, largest)
            else:
                sl = second(merged, i, i+1)
                best = max(best, sl, largest - d)
        return best