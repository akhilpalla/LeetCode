class Solution:
    def minAnagramLength(self, s: str) -> int:
        if not s: return
        N = len(s)
        def isPossible(targetIndex):
            required = Counter(s[:targetIndex])
            start = 0
            while start < N:
                current = Counter(s[start:start + targetIndex])
                if current != required:
                    return False
                start += targetIndex
            return True
        for i in range(1, N):
            if N % i == 0:
                if isPossible(i):
                    return i
        return N