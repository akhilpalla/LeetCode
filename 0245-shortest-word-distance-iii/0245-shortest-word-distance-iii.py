class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        seen = {}
        result = float('inf')
        for i,  w in enumerate(words):
            if word1 == w and word2 in seen:
                result = min(result, i - seen[word2])
            if word2 == w and word1 in seen:
                result = min(result, i - seen[word1])
            if word1 == w or word2 == w:
                seen[w] = i
        return result