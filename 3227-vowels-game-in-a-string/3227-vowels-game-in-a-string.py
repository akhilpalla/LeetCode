class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        vowel_count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_count += 1
                break
        if vowel_count:
            return True
        else:
            return False
        