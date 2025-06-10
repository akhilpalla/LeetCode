class Solution:
    def maxDifference(self, s: str) -> int:
        cntr = Counter(list(s))
        od, ev = 0, float('inf')
        for char in cntr:
            if cntr[char]%2:
                od = max(od, cntr[char])
            else:
                ev = min(ev, cntr[char])
        return od-ev