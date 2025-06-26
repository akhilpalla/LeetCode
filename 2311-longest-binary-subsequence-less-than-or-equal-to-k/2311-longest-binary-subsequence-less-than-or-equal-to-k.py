class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        if int(s, 2) <= k:
            return len(s)
        s = list(s)
        i = 0
        retLen = len(s)
        while int(''.join(s), 2) > k:
            if '1' == s[i]:
                retLen -= 1
                s[i] = '0'
            i += 1
        if int(''.join(s), 2) > k:
            return 0
        return retLen