class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        maxCols = float('-inf')
        for word in words:
            maxCols = max(len(word), maxCols)
        for i in range(maxCols):
            if words[i] != ''.join([word[i] for word in words if i < len(word)]):
                return False
        return True