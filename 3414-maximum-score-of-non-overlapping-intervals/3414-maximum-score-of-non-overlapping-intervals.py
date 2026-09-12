class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_right
        n = len(intervals)
        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )
        starts = [x[0] for x in arr]
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]
            for k in range(1, 5):
                skip = dp[i + 1][k]
                take_score, take_ids = dp[nxt[i]][k - 1]
                take = (take_score + w, tuple(sorted(take_ids + (idx,))))
                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip)
        return list(dp[0][4][1])