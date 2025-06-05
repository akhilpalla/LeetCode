class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = { c:c for c in map(chr, range(ord('a'), ord('z') + 1)) }

        def findRoot(c):
            while uf[c] != c:
                uf[c] = uf[uf[c]]
                c = uf[c]
            return c
        
        for i in range(len(s1)):
            r1 = findRoot(s1[i])
            r2 = findRoot(s2[i])
            if r1 < r2:
                uf[r2] = r1
            else:
                uf[r1] = r2
        
        return "".join([ findRoot(c) for c in baseStr ])