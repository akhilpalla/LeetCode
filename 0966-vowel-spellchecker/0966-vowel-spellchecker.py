class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        def getWildcard(s):
            return ''.join(['*' if c in vow else c for c in s])
        words, original = defaultdict(str), set()
        for w in wordlist:
            original.add(w)
            if w.lower() not in words:
                words[w.lower()] = w
            wildcard = getWildcard(w)
            if wildcard not in words:
                words[wildcard] = w
            if wildcard.lower() not in words:
                words[wildcard.lower()] = w
        res = []
        for q in queries:
            wildcard = getWildcard(q)
            lowerWildcard = wildcard.lower()
            currWord = q
            lowerWord = q.lower()
            if currWord in original:
                res += [q]
            elif lowerWord in words:
                res += [words[lowerWord]]
            elif wildcard in words:
                res += [words[wildcard]]
            elif lowerWildcard in words:
                res += [words[lowerWildcard]]
            else:
                res += [""]
        return res