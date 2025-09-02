class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i in range(n):
            for j in range(i + 1, n):
                if points[i][1] < points[j][1]: 
                    continue   
                valid = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if (points[k][0] >= points[i][0] and points[k][0] <= points[j][0] and
                        points[k][1] >= points[j][1] and points[k][1] <= points[i][1]):
                        valid = False
                        break
                if valid:
                    count += 1
        return count