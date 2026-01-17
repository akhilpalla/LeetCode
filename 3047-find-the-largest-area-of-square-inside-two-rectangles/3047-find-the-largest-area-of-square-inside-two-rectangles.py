class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        def intersection(a_bottom: list[int], a_top: list[int], b_bottom: list[int], b_top: list[int]) -> int:
            ax1, ay1 = a_bottom
            ax2, ay2 = a_top
            bx1, by1 = b_bottom
            bx2, by2 = b_top

            ix1 = max(ax1, bx1)
            iy1 = max(ay1, by1)
            ix2 = min(ax2, bx2)
            iy2 = min(ay2, by2)

            if ix1 >= ix2 or iy1 >= iy2:
                return 0

            side = min(ix2 - ix1, iy2 - iy1)
            return side * side


        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, intersection(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]))

        return res