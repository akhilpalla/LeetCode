class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row, col))
                    
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                next_x, next_y = x + dx, y + dy
                if m > next_x >= 0 and n > next_y >= 0 and rooms[next_x][next_y] == 2 ** 31 - 1:
                    rooms[next_x][next_y] = rooms[x][y] + 1
                    q.append((next_x, next_y))   