class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        positions = [0] * (len(s)+1)

        for w in words:
            match_list = self.search(s, w)
            for start in match_list:
                positions[start] += 1
                positions[start+len(w)] -= 1

        ans = int(bool(positions[0])) * '<b>' + s[0]
        for pointer in range(1, len(s)):
            positions[pointer] += positions[pointer-1]
            if positions[pointer] > 0 and positions[pointer-1] < 1:
                ans +=  '<b>'
            elif positions[pointer] < 1 and positions[pointer-1] > 0:
                ans +=  '</b>'

            ans += s[pointer]

        return ans + (int(bool(-positions[-1])) * '</b>')

    # return a list of all occurrence positions of pattern s in word w
    def search(self, s, w):
        res, pointer = [], 0
        while (occ := s.find(w, pointer)) != -1:
            res.append(occ)
            pointer = occ + 1

        return res