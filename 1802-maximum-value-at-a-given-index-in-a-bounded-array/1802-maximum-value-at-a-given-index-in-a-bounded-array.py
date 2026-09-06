class Solution:
    def maxValue(self, n, index, maxSum):
        maxSum -= n
        l, r = 0, maxSum
        while l != r:
            m = (l + r + 1) // 2
            s = max(0, m - index - 1)
            e = max(0, m - n + index)
            if m * m <= maxSum + (s * (s + 1) + e * (e + 1)) // 2: l = m
            else: r = m - 1
        return r + 1