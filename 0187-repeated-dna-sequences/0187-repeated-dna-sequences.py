from collections import Counter

class Solution:
    def inttostr(self, n: int) -> str:
        translation = 'ACGT'  
        s = ""
        for i in range(18, -2, -2):  
            s+= translation[(n >> i) & 3]
        return s

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        translation = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        visited = dict()

        it = iter(s)
        n = 0
        for i in range(0,10):
            n = (n<<2) + translation[next(it)]
        visited[n] = 1

        mask = (1<<18)-1
        while c := next(it, None):
            n = ((n & mask)<<2) + translation[c]
            visited[n] = visited.get(n, 0) + 1

        return list([self.inttostr(n) for n, cnt in visited.items() if cnt > 1])

      