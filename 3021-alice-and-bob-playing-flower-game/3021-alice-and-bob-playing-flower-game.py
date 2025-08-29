class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2 + n % 2) * (m // 2) + (m // 2 + m % 2) * (n // 2)

        
"""
how many pairs from [1, n] and [1, m] make an odd number
"""