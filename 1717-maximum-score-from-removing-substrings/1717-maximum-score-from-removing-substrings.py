class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def processAB(s: str, x: int, y: int) -> int:
            stk = []
            ans = 0
            for char in s:
                if stk and stk[-1] == 'a' and char == 'b':
                    stk.pop()
                    ans += x
                else:
                    stk.append(char)
            a = stk.count('a')
            b = stk.count('b')
            return min(a, b) * y + ans
        
        def processBA(s: str, x: int, y: int) -> int:
            stk = []
            ans = 0
            for char in s:
                if stk and stk[-1] == 'b' and char == 'a':
                    stk.pop()
                    ans += y
                else:
                    stk.append(char)
            a = stk.count('a')
            b = stk.count('b')
            return min(a, b) * x + ans
        
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] != 'a' and s[i] != 'b':
                i += 1
                continue
            j = i
            t = ""
            while j < n and (s[j] == 'a' or s[j] == 'b'):
                t += s[j]
                j += 1
            ans += max(processAB(t, x, y), processBA(t, x, y))
            i = j
        return ans