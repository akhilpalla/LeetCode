class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        n: int = len(s)
        one: int = 0
        zero: int = 0
        i: int = 0
        build: list[str] = []
        for j in range(n):
            if s[j] == '1': one += 1
            else: zero += 1
            if one == zero:
                build.append('1' + self.makeLargestSpecial(s[i + 1: j]) + '0')
                i = j + 1
        build.sort(reverse=True)
        return ''.join(build)