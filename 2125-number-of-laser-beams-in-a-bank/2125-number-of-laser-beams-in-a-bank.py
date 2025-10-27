class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for str in bank:
            curr = 0
            for ch in str:
                if ch == '1':
                    curr += 1
            if curr > 0:
                ans += prev * curr
                prev = curr
        return ans