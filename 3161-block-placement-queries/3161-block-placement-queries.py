from sortedcontainers import SortedList

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def query(self, i):
        res = 0

        while i > 0:
            res = max(res, self.tree[i])
            i -= i & -i

        return res


class Solution:
    def getResults(self, queries):
        LIMIT = min(50000, len(queries) * 3)

        obstacles = SortedList([0, LIMIT])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = FenwickTree(LIMIT + 2)
        obs = list(obstacles)

        for i in range(len(obs) - 1):
            left = obs[i]
            right = obs[i + 1]
            bit.update(right, right - left)

        ans = []

        for q in reversed(queries):

            if q[0] == 1:
                x = q[1]

                idx = obstacles.bisect_left(x)
                left = obstacles[idx - 1]
                right = obstacles[idx + 1]
                bit.update(right, right - left)
                obstacles.remove(x)

            else:
                _, x, sz = q

                idx = obstacles.bisect_right(x)
                prev_obstacle = obstacles[idx - 1]
                best = bit.query(prev_obstacle)

                ans.append(
                    best >= sz or
                    x - prev_obstacle >= sz
                )

        return ans[::-1]