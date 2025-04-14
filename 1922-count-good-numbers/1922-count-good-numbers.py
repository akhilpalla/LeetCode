class Solution:
    mod = 10**9 + 7   
    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2   
        odd = n // 2          

        return pow(5, even, self.mod) * pow(4, odd, self.mod) % self.mod