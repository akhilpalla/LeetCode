class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        n = len(s)
        counter = Counter(s)
        def backtrack(curr, idx, useAny):
            nonlocal ans
            if idx == n:
                if curr > t:
                    ans = curr
                    return True
                return False
            for c in string.ascii_lowercase:
                if not useAny:
                    if c < t[idx]:
                        continue
                if not counter[c]:
                    continue
                counter[c] -= 1
                if backtrack(curr + c, idx + 1, useAny or (c > t[idx])):
                    return True
                counter[c] += 1

            return False
        ans = ''
        backtrack('', 0, False)
        return ans