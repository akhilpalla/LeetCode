class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dis = 0
        for x, y in enumerate(colors):
            if y != colors[0]:
                dis = max(dis, x)
            if y != colors[-1]:
                dis = max(dis, len(colors) - 1 - x)
        return dis