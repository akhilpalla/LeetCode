class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        def dfs(idx, prefix, count):
            if idx == len(word):
                if count > 0:
                    prefix += str(count)
                result.append(prefix)
                return
            dfs(idx + 1, prefix, count + 1)
            if count > 0:
                prefix += str(count)
            dfs(idx + 1, prefix + word[idx], 0)
        dfs(0, "", 0)
        return result
