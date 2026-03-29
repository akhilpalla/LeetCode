class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def count(string):
            odd = Counter()
            even = Counter()
            for i, c in enumerate(string):
                if i & 1:
                    odd[c] += 1
                else:
                    even[c] += 1
            return odd, even
        def compare(x, y):
            xodd, xeven = x
            yodd, yeven = y
            return xodd == yodd and xeven == yeven
        return compare(count(s1), count(s2))