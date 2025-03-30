class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def match(s1, s2):
            i = 0        
            j = 0       
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i

        res = 0

        while target:
            ind = match(target, source)
            if ind == 0:
                return -1
            res += 1
            target = target[ind:]

        return res