class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def findMaxEdge(bars: List[int]) -> int:
            bars.sort()
            floor, prev, maxEdge = 1, -1, 1
            for bar in bars:
                if prev < bar - 1:
                    floor = bar - 1
                maxEdge = max(maxEdge, bar + 1 - floor)
                prev = bar
            return maxEdge
        edge = min(findMaxEdge(hBars), findMaxEdge(vBars))
        return edge*edge