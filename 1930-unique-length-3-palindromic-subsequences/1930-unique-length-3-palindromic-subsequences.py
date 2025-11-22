class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        c, ans = Counter(s), 0                             # <-- 1)
        doubles = {ch for ch in c if c[ch] > 1}

        for ch in doubles:                              
            ans+= len(set(s[s.find(ch)+1:s.rfind(ch)]))    # <-- 2) and 3)

        return ans