class Solution:
    def makeFancyString(self, s: str) -> str:
        l = [s[:2]]

        for i in range(2, len(s)):
            if not(s[i] == s[i-1] == s[i-2]):
                l.append(s[i])
        
        return "".join(l)