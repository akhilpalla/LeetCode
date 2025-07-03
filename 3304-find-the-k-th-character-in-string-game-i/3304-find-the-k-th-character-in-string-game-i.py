class Solution:
    def kthCharacter(self, k: int) -> str:
        curr = "a"   

        while len(curr) < k:
            temp = ""
            for ch in curr:
                next_ch = 'a' if ch == 'z' else chr(ord(ch) + 1)
                temp += next_ch
            curr += temp   

        return curr[k - 1]   