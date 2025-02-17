class Solution:
    def __init__(self):
        self.alreadySeen = {}

    def getSignature(self, s):
        signature = {}
        for c in s:
            if not c in signature:
                signature[c] = 0
            signature[c] += 1
        return signature

    def sameSignature(self, s1, s2):
        signature1 = self.getSignature(s1)
        signature2 = self.getSignature(s2)
        return signature1 == signature2

    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if not self.sameSignature(s1, s2):
            return False
        key = (s1, s2)
        if key in self.alreadySeen:
            return self.alreadySeen[key]
        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.alreadySeen[key] = True
                return True
            j = n-i
            if self.isScramble(s1[i:], s2[:j]) and self.isScramble(s1[:i], s2[j:]):
                self.alreadySeen[key] = True
                return True
        self.alreadySeen[key] = False
        return False
        
        