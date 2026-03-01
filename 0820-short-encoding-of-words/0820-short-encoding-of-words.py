class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x : -len(x))
        lookup = set()
        res = 0
        for word in words:
            if word in lookup:
                continue
            res += len(word) + 1
            for x in range(1, len(word)+1):
                lookup.add(word[-x:])
        return res
                