class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n ==  3:
            return 5
        que = [1,2,5]
        for i in range(3, n):
            current = (2 * que[-1]) + que.pop(0)
            que.append(current)
        return que[2] % (10**9 + 7)