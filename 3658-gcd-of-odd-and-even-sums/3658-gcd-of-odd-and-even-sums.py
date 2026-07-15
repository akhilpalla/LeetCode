class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        so,se=0,0
        for i in range(1,2*n+1):
            if i%2==0:
                se+=i
            else:
                so+=i
        return math.gcd(so,se)