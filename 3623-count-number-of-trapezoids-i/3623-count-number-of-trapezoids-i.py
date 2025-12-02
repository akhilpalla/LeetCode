class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 1000000007
        d = Counter(y for _,y in points)
        ans = 0
        y_points = tuple(v * (v-1) // 2 for v in d.values())
        s = sum(y_points)
        for y in y_points:
            s -= y
            ans += y * s
        return ans % mod