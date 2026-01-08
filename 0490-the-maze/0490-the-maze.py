class Solution:
   def hasPath(self, maze: List[List[int]], start: List[int], end: List[int]) -> bool:
       rows, cols = len(maze), len(maze[0]) 
       visited = set()
       queue = deque([tuple(start)])
       
       while queue:
           curr_x, curr_y = queue.popleft()
           
           if [curr_x, curr_y] == end:
               return True
               
           for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
               x, y = curr_x, curr_y
               
               # Roll the ball until hitting wall/border
               while 0 <= x+dx < rows and 0 <= y+dy < cols and maze[x+dx][y+dy] == 0:
                   x += dx
                   y += dy
                   
               if (x,y) not in visited:
                   visited.add((x,y))
                   queue.append((x,y))
                   
       return False

# T = MN * (M+N) at each point we will go to the extreme end and bottom in all 4 dirs
# S = NM