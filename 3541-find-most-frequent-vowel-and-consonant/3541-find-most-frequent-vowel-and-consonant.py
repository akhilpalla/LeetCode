class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0] * 26
        maxvowel = 0
        maxconsonant = 0
        for c in s:
            index = ord(c) - ord('a')
            freq[index] += 1
            if c in "aeiou":
                maxvowel = max(maxvowel, freq[index])
            else:
                maxconsonant = max(maxconsonant, freq[index])
        return maxvowel + maxconsonant
