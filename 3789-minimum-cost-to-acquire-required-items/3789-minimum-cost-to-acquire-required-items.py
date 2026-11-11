class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 == 0 and need2 == 0:
            return 0
        res = 0
        k = min(need1, need2)
        if costBoth <= cost1 + cost2:
            res += k * costBoth
            need1 -= k
            need2 -= k
        res += need1 * min(cost1, costBoth)
        res += need2 * min(cost2, costBoth)
        return res