class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefs = defaultdict(set)
        n = len(words[0])
        result = []
        for w in words:
            for i in range(n):
                prefs[w[:i]].add(w)

        def back_track(path):
            if len(path) == n:
                result.append(path)

            else:
                prefix = "".join(w[len(path)] for w in path)
                for w in prefs[prefix]:
                    back_track(path + [w])

        back_track([])
        return result
                