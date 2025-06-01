class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if (n // 3) > limit:
            return 0

        def count_ways(a):
            if a == n:
                return 1

            goal = n - a

            if 2 * limit < goal:
                return 0
            elif 2 * limit == goal:
                return 1
            elif limit >= goal:
                return goal + 1
            else:
                return 2 * limit - goal + 1
    
        ways = 0
        for i in range(min(limit + 1, n + 1)):
            ways += count_ways(i)

        return ways
        