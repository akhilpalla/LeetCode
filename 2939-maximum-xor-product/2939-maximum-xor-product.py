class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a < b:
            a, b = b, a
        
        m = (a >> n << n)
        t = (b >> n << n)
        
        if m != t:
            firstdiff = False
        else:
            firstdiff = True

        stra = format(a, f'0{n}b')[-n:]
        strb = format(b, f'0{n}b')[-n:]
        for i, (x,y) in enumerate(zip(stra, strb)):
            if n-1-i >= 0:
                if x == y:
                    m += 2 ** (n-1-i)
                    t += 2 ** (n-1-i)
                else:
                    if firstdiff:
                        m += 2 ** (n-1-i)
                        firstdiff = False
                    else:
                        t += 2 ** (n-1-i)
                        
        return m*t % (10**9 + 7)