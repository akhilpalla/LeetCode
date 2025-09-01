class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        N, M = len(workers), len(bikes)
        arr = [[0] * N for _ in range(M)]
        for i, (x, y) in enumerate(bikes):
            for j, (xx, yy) in enumerate(workers):
                arr[i][j] = abs(x - xx) + abs(y - yy)
        GOOD = (1 << N) - 1
        INF = 10 ** 10
        @cache
        def calc(index, mask):
            if index == M:
                if mask == GOOD:
                    return 0
                return INF
            if mask == GOOD:
                return 0
            best = calc(index + 1, mask)
            for j in range(N):
                if not (2 ** j) & mask:
                    best = min(best, calc(index + 1, mask | (2 ** j)) + arr[index][j])
            return best
        return calc(0, 0)