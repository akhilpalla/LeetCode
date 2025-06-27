from collections import Counter
from itertools import combinations, permutations

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSub(source, target):
            target = iter(target)
            return all(ch in target for ch in source)

        result = ""
        subseq = set()
        domain = "".join(ch * (val // k) for ch, val in Counter(s).items())

        for i in range(len(domain) + 1):
            for cmb in combinations(domain, i):
                for per in permutations(cmb):
                    subseq.add("".join(per))

        sourceOfPossibleSubSeq = sorted(subseq, key=lambda x: (len(x), x), reverse=True)
        for seq in sourceOfPossibleSubSeq:
            if isSub(seq * k, s):
                return seq
        return result