class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0 )]
        distance = [[float('inf')] * n for _ in range(m)]
        distance[ball[0]][ball[1]] = 0
        minHeap = [(0, '', ball[0], ball[1])]
        pathRecord = [[''] * n for _ in range(m)]

        while minHeap:
            d, path, x, y = heapq.heappop(minHeap)
            if [x, y] == hole:
                return path
            for direction, dx, dy in directions:
                steps, nx, ny = 0, x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    steps += 1
                    if [nx, ny] == hole:
                        break
                if d + steps < distance[nx][ny] or (d + steps == distance[nx][ny] and path + direction < pathRecord[nx][ny]):
                    distance[nx][ny] = d + steps
                    pathRecord[nx][ny] = path + direction
                    heapq.heappush(minHeap, (d + steps, path + direction, nx, ny))
        
        return 'impossible'