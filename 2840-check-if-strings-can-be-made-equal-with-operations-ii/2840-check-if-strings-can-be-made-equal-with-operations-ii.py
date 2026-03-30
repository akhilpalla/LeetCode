class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odds = [0] * 26
        evens = [0] * 26

        for i in range(0, len(s1), 2):
            evens[ord(s1[i]) - ord('a')] += 1
            evens[ord(s2[i]) - ord('a')] -= 1

        for i in range(1, len(s1), 2):
            odds[ord(s1[i]) - ord('a')] += 1
            odds[ord(s2[i]) - ord('a')] -= 1

        return all([v == 0 for v in odds]) and all([v == 0 for v in evens])