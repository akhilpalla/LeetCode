def add(s, a):
    return ''.join([str((int(x) + a)%10) if i%2==1 else x for i, x in enumerate(s)])

def move(s, b):
    return ''.join([s[i - b] for i in range(len(s))])

class Solution:
    def dp(self, s):
        if s in self.visited:
            return
        if int(self.min_s) > int(s):
            self.min_s = s
        self.visited.add(s)        
        self.dp(add(s, self.a))        
        self.dp(move(s, self.b))              
        
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.visited = set()
        self.min_s = s
        self.a = a
        self.b = b
        self.dp(s)
        return self.min_s