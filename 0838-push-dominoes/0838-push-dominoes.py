class Solution:
    
    def __init__(self):
        self.mem = dict()
    
    def RSFL(self, i, st, l):
        if i >= l:
            return 'N', 0
        if (i, 'R') in self.mem:
            return self.mem[(i, 'R')]
        if st[i] == 'L':
            return 'L', 0
        elif st[i] == 'R':
            return 'R', 0
        lor, dist = self.RSFL(i + 1, st, l)
        if lor == 'N':
            ans  = 'N', 0
        else:
            ans = lor, dist + 1
        self.mem[(i, 'R')] = ans
        return ans
        
    def LSFR(self, i, st, l):
        if i < 0:
            return 'N', 0
        if (i, 'L') in self.mem:
            return self.mem[(i, 'L')]
        if st[i] == 'L':
            return 'L', 0
        elif st[i] == 'R':
            return 'R', 0
        lor, dist = self.LSFR(i - 1, st, l)
        if lor == 'N':
            ans = 'N', 0
        else:
            ans = lor, dist + 1
        self.mem[(i, 'L')] = ans
        return ans
    
    def Util(self, st, ind, l, new):
        if ind >= l:
            return
        if st[ind] == 'L':
            new[ind] = 'L'
            self.Util(st, ind + 1, l, new)
            return
        elif st[ind] == 'R':
            new[ind] = 'R'
            self.Util(st, ind + 1, l, new)
            return
        leftVal, distL = self.LSFR(ind, st, l)
        rightVal, distR = self.RSFL(ind, st, l)
        if leftVal == 'R' and rightVal == 'R':
            new[ind] = 'R'
        elif leftVal == 'L' and rightVal == 'L':
            new[ind] = 'L'
        elif leftVal == 'N' and rightVal == 'L':
            new[ind] = 'L'
        elif leftVal == 'R' and rightVal == 'N':
            new[ind] = 'R'
        elif leftVal == 'R' and rightVal == 'L' and distL > distR:
            new[ind] = 'L'
        elif leftVal == 'R' and rightVal == 'L' and distL < distR:
            new[ind] = 'R'
        self.Util(st, ind + 1, l, new)
            
    
    def pushDominoes(self, dominoes: str) -> str:
        l = len(dominoes)
        new = ['.' for i in range(l)]
        self.Util(dominoes, 0, l, new)
        return ''.join(new)