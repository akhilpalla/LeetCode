class Solution:
    def totalMoney(self, n: int) -> int:
        div = n // 7
        rem = n % 7
        ans = ((7 * 8) // 2) * div + 7 * ((div * (div - 1)) // 2)
        ans += ((rem * (rem + 1)) // 2) + (div * rem)
        return ans