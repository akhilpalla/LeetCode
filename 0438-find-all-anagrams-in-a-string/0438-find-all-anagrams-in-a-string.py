ALPHABET_LENGTH = 26

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sn = len(s)
        pn = len(p)
        result = []
        if sn < pn:
            return result
        p_arr = [0]*ALPHABET_LENGTH
        s_arr = [0]*ALPHABET_LENGTH
        ord_a = ord("a")
        for i in range(pn):
            p_arr[ord(p[i]) - ord_a] += 1
            s_arr[ord(s[i]) - ord_a] += 1
        if p_arr == s_arr:
            result.append(0)
        for i in range(1, sn - pn + 1):
            tail_idx = i -1
            tail = s[tail_idx]
            head_idx = tail_idx + pn
            head = s[head_idx]
            if tail == head:
                if len(result) > 0 and result[-1] == i - 1:
                    result.append(i)
                continue
            s_arr[ord(tail) - ord_a] -= 1
            s_arr[ord(head) - ord_a] += 1
            if p_arr == s_arr:
                result.append(i)
        return result