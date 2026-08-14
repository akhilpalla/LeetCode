class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = [0] * 26
        res = i = j = 0
        for i in range(len(s)):
            cnt[ord(s[i]) - ord('a')] += 1
            while cnt[ord(s[i]) - ord('a')] > 2:
                cnt[ord(s[j]) - ord('a')] -= 1
                j += 1
            res = max(res, i - j + 1)
        return res