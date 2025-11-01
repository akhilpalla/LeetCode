class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        s, w, h, m = sideLength, max(width, height), min(width, height), maxOnes
        ans = (w//s)*(h//s)*m + min((w%s)*(h%s), m )*(h//s+w//s+1)
        m -= min((w%s)*(h%s), m )
        if m>0:
            ans += (w//s)*min(m, (h%s)*(s - w%s) )
            m -= min(m, (h%s)*(s - w%s) )
        if m>0:
            ans += (h//s)* min(m, (w%s)*(s - h%s))
        return ans