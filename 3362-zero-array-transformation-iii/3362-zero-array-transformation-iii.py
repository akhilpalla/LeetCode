from sortedcontainers import SortedList

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(key=lambda q: q[0])

        d = [0] * (n + 1)
        hp = []
        cnt = 0
        j = 0
        for i in range(n):
            while j < len(queries) and queries[j][0] <= i:
                heappush(hp, -queries[j][1])
                j += 1
            k = 0
            cnt += d[i]
            while cnt < nums[i]:
                if len(hp) == 0:
                    break
                e = -heappop(hp)
                if e < i:
                    break
                cnt += 1
                d[e+1] += -1
            if cnt < nums[i]:
                return -1
        return len(hp)