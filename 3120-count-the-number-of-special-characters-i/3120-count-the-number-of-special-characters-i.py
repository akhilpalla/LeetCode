class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l, u = [0]*26, [0]*26
        for c in word:
            if c.islower(): l[ord(c)-ord('a')] = 1  
            else: u[ord(c)-ord('A')] = 1             
        return sum(1 for i in range(26) if l[i] and u[i])  