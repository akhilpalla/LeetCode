class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left = ""
        mid = ""
        for ch in sorted(count.keys()):
            freq = count[ch]
            if freq % 2 != 0:
                mid = ch
                freq -= 1
            left += (ch * (freq // 2))
        right = left[ : : -1]
        return left + mid + right