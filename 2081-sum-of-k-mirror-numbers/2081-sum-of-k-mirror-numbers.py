class Solution:
    def check_k(self, num, k):
        temp = []
        while num >= k:
            temp.append(str(num % k))
            num //= k
        temp.append(str(num))
        return temp == temp[::-1]

    def kMirror(self, k, n):
        ans = 0
        for i in range(1, 10):
            if n == 0:
                return ans
            if self.check_k(i, k):
                ans += i
                n -= 1

        l = 2
        while n > 0:
            pal_length = (l + 1) // 2
            s = 10 ** (pal_length - 1)
            e = 10 ** pal_length
            for dig in range(s, e):
                temp = str(dig)
                if l % 2 == 0:
                    mirror = temp + temp[::-1]
                else:
                    mirror = temp + temp[:-1][::-1]
                val = int(mirror)
                if self.check_k(val, k):
                    ans += val
                    n -= 1
                    if n == 0:
                        return ans
            l += 1
        return ans