class Solution:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        R, C = len(image), len(image[0])
        fr = lambda r: any(image[r][c] == '1' for c in range(C))
        fc = lambda c: any(image[r][c] == '1' for r in range(R))
        h = (R - bisect_left(range(r), 1, key=fr) -
             bisect_left(range(R-1, r, -1), 1, key=fr))
        w = (C - bisect_left(range(c), 1, key=fc) -
             bisect_left(range(C-1, c, -1), 1, key=fc))
        return h * w