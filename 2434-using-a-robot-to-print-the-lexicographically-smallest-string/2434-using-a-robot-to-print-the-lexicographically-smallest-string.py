class Solution:
    def robotWithString(self, s: str) -> str:
        ord_a = ord('a')
        freqs = self.count_freqs(s)
        paper = []
        t = []

        i = 0
        ci = 0
        while i < len(freqs):
            if freqs[i] <= 0:
                i += 1
            else:
                while t and ord(t[-1]) - ord_a <= i:
                    paper.append(t.pop())

                while ord(s[ci]) - ord_a != i:
                    freqs[ord(s[ci]) - ord_a] -= 1
                    t.append(s[ci])
                    ci += 1
                
                freqs[ord(s[ci]) - ord_a] -= 1
                t.append(s[ci])
                ci += 1

                paper.append(t.pop())
                
        while t:
            paper.append(t.pop())
        return "".join(paper)

    def count_freqs(self, s: str) -> list:
        freqs = [0 for _ in range(26)]
        ord_a = ord('a')
        for c in s:
            freqs[ord(c)-ord_a] += 1
        return freqs 