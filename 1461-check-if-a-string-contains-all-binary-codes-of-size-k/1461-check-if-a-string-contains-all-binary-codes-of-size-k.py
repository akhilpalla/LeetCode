class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        segments = set()  
        for i in range(len(s)-k+1):
            segment = s[i:i+k]
            segments.add(segment)
        if len(segments) < 2**k:
            return False
        return True