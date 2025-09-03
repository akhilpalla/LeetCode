class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x: (x[0], -x[1]))

        for i in range(len(points) - 1):
            point_A = points[i]
            xMin = point_A[0] - 1
            yMin = -math.inf
            xMax = math.inf
            yMax = point_A[1] + 1

            for j in range(i + 1, len(points)):
                point_B = points[j]
                if point_B[0] > xMin and point_B[1] > yMin and point_B[0] < xMax and point_B[1] < yMax:
                    ans += 1
                    xMin = point_B[0]
                    yMin = point_B[1]
        return ans