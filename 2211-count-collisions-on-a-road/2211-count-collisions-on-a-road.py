class Solution:
    def countCollisions(self, directions: str) -> int:
        temp = []
        for dire in directions:
            temp.append(dire)
        directions = temp
        n = len(directions)
        if n == 0 or n == 1:
            return 0
        ans = 0
        # while 
        for i in range(1,n):
            if directions[i-1] == "R" and directions[i] == "L":
                ans += 2
                directions[i] = "S"
                directions[i-1] = "S"
            elif directions[i-1] == "R" and directions[i] == "S":
                ans += 1
                directions[i] = "S"
                directions[i-1] = "S"
            elif directions[i-1] == "S" and directions[i] == "L":
                ans += 1
                directions[i] = "S"
                directions[i-1] = "S"
        for i in range(n-2,-1,-1):
            if directions[i] == "R" and directions[i+1] == "L":
                ans += 2
                directions[i+1] = "S"
                directions[i] = "S"
            elif directions[i] == "R" and directions[i+1] == "S":
                ans += 1
                directions[i+1] = "S"
                directions[i] = "S"
            elif directions[i] == "S" and directions[i+1] == "L":
                ans += 1
                directions[i+1] = "S"
                directions[i] = "S"
                
        return ans