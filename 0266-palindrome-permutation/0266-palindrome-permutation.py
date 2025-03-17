class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bag = 0
        for c in s:
            bag ^= (1 << ord(c) - ord("a"))
        count = 0
        while bag:
            bag = bag & (bag - 1)
            count += 1
        return 0 == count or 1 == count