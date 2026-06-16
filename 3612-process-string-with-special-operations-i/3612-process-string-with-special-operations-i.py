class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif result and c == '*':
                result.pop()
            elif result and c == '#':
                result.extend(result)
            elif result:
                result.reverse()
        return ''.join(result)