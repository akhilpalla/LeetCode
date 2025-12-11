class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        cols = [[] for _ in range(n+1)]
        rows = [[] for _ in range(n+1)]
        for i, j in buildings:
            cols[j].append(i)
            rows[n-i+1].append(j)
        for i in range(1,len(cols)):
            if cols[i]:
                mi, ma = min(cols[i]), max(cols[i])
                cols[i][0], cols[i][-1] = mi, ma
            else:
                cols[i].append(-1)
        for i in range(1,len(rows)):
            if rows[i]:
                mi, ma = min(rows[i]), max(rows[i])
                rows[i][0], rows[i][-1] = mi, ma
            else:
                rows[i].append(-1)
        cnt = 0
        for i, j in buildings:
            if rows[n-i+1][0] < j < rows[n-i+1][-1] and cols[j][0] < i < cols[j][-1]:
                cnt += 1
        return cnt