import bisect
from typing import List

class Solution:
    def getCount(self, walls, left, right):
        if left > right:
            return 0
        idx1 = bisect.bisect_left(walls, left)
        idx2 = bisect.bisect_right(walls, right)
        return idx2 - idx1

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robotList = [(robots[i], distance[i]) for i in range(n)]
        robotList.sort()
        walls.sort()

        # add sentinel just like C++
        robotList.append((10**9, 0))

        dp = [[0] * 2 for _ in range(n)]  # only n, not n+1

        # base case
        dp[0][0] = self.getCount(walls, robotList[0][0] - robotList[0][1], robotList[0][0])
        dp[0][1] = self.getCount(walls,
                                 robotList[0][0],
                                 min(robotList[1][0] - 1, robotList[0][0] + robotList[0][1]))

        # transition
        for i in range(1, n):
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + self.getCount(
                walls,
                robotList[i][0],
                min(robotList[i+1][0] - 1, robotList[i][0] + robotList[i][1])
            )

            dp[i][0] = dp[i-1][0] + self.getCount(
                walls,
                max(robotList[i-1][0] + 1, robotList[i][0] - robotList[i][1]),
                robotList[i][0]
            )

            res = dp[i-1][1] \
                + self.getCount(walls,
                                max(robotList[i-1][0] + 1, robotList[i][0] - robotList[i][1]),
                                robotList[i][0]) \
                - self.getCount(walls,
                                max(robotList[i-1][0], robotList[i][0] - robotList[i][1]),
                                min(robotList[i][0] - 1, robotList[i-1][0] + robotList[i-1][1]))
            dp[i][0] = max(dp[i][0], res)

        return max(dp[n-1][0], dp[n-1][1])