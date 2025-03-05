class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def is_vowel(char):
            vowels = "aeiou"
            return char in vowels
        
        if k == 0:
            d = {'a': -math.inf, 'e': -math.inf, 'i':-math.inf, 'o':-math.inf, 'u':-math.inf}
            temp = d.copy()
            ans, mn  = 0, -math.inf
            hold = 0
            for i, j in enumerate(word):
                if not is_vowel(j):
                    temp = d.copy()
                    mn = math.inf
                    hold = i + 1
                    continue
                temp[j] = i
                mn = min(temp.values())
                if mn >= hold and (mn != -math.inf):
                    ans += (mn - hold + 1)
            return ans

        
        cs = []
        for i, j in enumerate(word):
            if not is_vowel(j):
                cs.append(i)
        ans = 0
        d = {'a':-1, 'e':-1, 'i':-1, 'o':-1, 'u':-1}
        n = 0
        for i, j in enumerate(word):
            if j in d:
                d[j] = i
            ind = bisect_right(cs, i)
            if ind < k:
                continue
            left = (cs[ind - k - 1] + 1 if ind - k - 1 >= 0 else 0)
            right = cs[ind - k]
            mn = min(min(d.values()), right)
            if left <= mn:
                val = (mn - left + 1)
                ans += val
        return ans