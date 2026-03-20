class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0]  * (m - k + 1) for _ in range(n - k + 1)]
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                arr = []
                for l in range(k):
                    arr.extend(grid[i+l][j: j+k])
                arr.sort()
                d = arr[-1] - arr[0]
                if d > 0:
                    for l in range(len(arr)-1):
                        t = arr[l+1] - arr[l]
                        if t > 0 and d > t:
                            d = t
                ans[i][j] = d
        return ans