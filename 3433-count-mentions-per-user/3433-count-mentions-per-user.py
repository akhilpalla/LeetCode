class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        cnt = 0
        here = []
        ans = [0] * n
        for op, time, info in events:
            if op == "MESSAGE":
                if info == "ALL":
                    cnt += 1
                elif info == "HERE":
                    cnt += 1
                    here.append(int(time))
                else:
                    for s in info.split():
                        ans[int(s[2:])] += 1
        for i in range(n):
            ans[i] += cnt
        here.sort()
        for op, time, info in events:
            if op == "OFFLINE":
                t = int(time)
                i = bisect_left(here, t)
                j = bisect_left(here, t + 60)
                ans[int(info)] -= j - i
        return ans