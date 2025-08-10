class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def power(num):
            l, r = 0, int(num ** 0.5) + 1
            while l <= r:
                m = (l + r) // 2
                val = 2 ** m
                if val == num:
                    return num
                elif val > num:
                    r = m - 1
                else:
                    l = m + 1
            return False
        a = str(n)
        leny = len(a)
        dic = {}
        for ch in a:
            dic[ch] = dic.get(ch, 0) + 1
        arr = []
        i = 1
        while len(str(i)) <= leny:
            if len(str(i)) == leny and power(i):
                arr.append(str(i))
            i *= 2
        for val in arr:
            copyy = dic.copy()
            flag = True
            for digit in val:
                if digit not in copyy or copyy[digit] == 0:
                    flag = False
                    break
                copyy[digit] -= 1
            if flag:
                return True
        return False