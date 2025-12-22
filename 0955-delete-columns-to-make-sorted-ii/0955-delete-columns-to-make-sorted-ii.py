class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n: int = len(strs)
        m: int = len(strs[0])
        seen: list[bool] = [False] * n
        output: int = 0
        for j in range(m):
            is_valid: bool = True
            for i in range(n - 1):
                if not seen[i] and strs[i][j] > strs[i + 1][j]: is_valid = False
            if is_valid:
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]: seen[i] = True
            else: output += 1
        return output