class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        if n == 2: return 0 if s[0] <= s[1] else -1
        s_char, b_char = min(s), max(s)
        if all(s[i] <= s[i+1] for i in range(n-1)):
            return 0
        if s[0] == b_char and s[-1] == s_char:
            if s.count(s_char) > 1 or s.count(b_char) > 1:
                return 2
            return 3
        if s[0] == s_char or s[-1] == b_char:
            return 1
        return 2