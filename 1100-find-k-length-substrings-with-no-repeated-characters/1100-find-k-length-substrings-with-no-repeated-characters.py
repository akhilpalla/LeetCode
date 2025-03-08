class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        unique = 0
        for i in range(0, len(s)-k+1):
            if len(set(s[i:i+k])) == len(s[i:i+k]):
                unique += 1
        
        return unique