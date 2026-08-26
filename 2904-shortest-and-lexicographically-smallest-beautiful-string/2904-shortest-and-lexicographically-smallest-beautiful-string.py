class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        ii = 0 
        for i, ch in enumerate(s): 
            if ch == '1': k -= 1
            while k < 0 or ii < i and s[ii] == '0': 
                if s[ii] == '1': k += 1
                ii += 1
            if k == 0 and (ans == '' or len(ans) > i-ii+1 or len(ans) == i-ii+1 and ans > s[ii : i+1]): ans = s[ii : i+1]
        return ans 