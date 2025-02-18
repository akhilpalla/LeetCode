class Solution:
    def longestCommonPrefix(self, s, t):
        i, j = 0, 0   
        while i < len(s) and j < len(t):
            if s[i] == t[j]:   
                i += 1
                j += 1
            else:
                if i != j:   
                    break
                i += 1   
        return j   