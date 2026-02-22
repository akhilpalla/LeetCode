class Solution:
    def binaryGap(self, n: int) -> int:
        if n.bit_count() < 2:   
            return 0
        while n & 1 == 0:   
            n >>= 1
        zeros = bin(n)[2:].split('1')   
        m = 0
        for z in zeros:  
            if len(z) > m:
                m = len(z)
        return m+1   