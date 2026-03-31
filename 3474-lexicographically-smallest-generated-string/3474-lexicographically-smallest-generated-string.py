class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        str2 = list(str2)
        n, m = len(str1), len(str2)

        word = ['#'] * (n + m - 1)
        for i in range(n - 1, -1, -1):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] == '#':
                        word[i+j] = str2[j]
                    elif word[i+j] != str2[j]:
                        return ""
        
        wildcard = set(i for i, c in enumerate(word) if c == '#')
        word = [c if c != '#' else 'a' for c in word]

        for i in range(n):
            if str1[i] == 'F' and word[i:i+m] == str2:
                for j in range(m - 1, -1, -1):
                    if i + j in wildcard and word[i+j] != 'z':
                        word[i+j] = chr(ord(word[i+j]) + 1)
                        break
                else:
                    return ""
        return "".join(word)