class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        ans = [words[0]]
        j = 0

        for i in range(1, n):
            if groups[i] != groups[j]:
                ans.append(words[i])
                j = i
        return ans