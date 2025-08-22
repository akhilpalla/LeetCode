class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        ans = set()
        prefix = {}
        suffix = {}
        for i, x in enumerate(phrases): 
            words = x.split()
            for j in prefix.get(words[-1], []): 
                ans.add(x[:-len(words[-1])] + phrases[j])
            for j in suffix.get(words[0], []): 
                ans.add(phrases[j] + x[len(words[0]):])
            prefix.setdefault(words[0], []).append(i)
            suffix.setdefault(words[-1], []).append(i)
        return sorted(ans)