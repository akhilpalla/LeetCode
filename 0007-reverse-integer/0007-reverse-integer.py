class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)

        while x != 0:
            pop = x % 10
            x //= 10

            # Check for overflow conditions
            # We check for overflow before multiplying because multiplying by 10 and adding a digit could cause an integer overflow. By checking the 
            # conditions in advance, we ensure that the multiplication won't push the result beyond the 32-bit signed integer limit.

            # max positive ==>  2^31 - 1 ==>  2147483647
            # max negative ==> -2^31     ==> −2147483648

            # we should also check the corner case where pop is 7 or 8 because they are last possible in the range

            # if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and pop > 7):
            #     return 0
            # if rev < (-2**31) // 10 or (rev == (-2**31) // 10 and pop < -8):
            #     return 0


            if rev > (INT_MAX) // 10 or (rev == (INT_MAX) // 10 and (INT_MAX%10) > 7):
                return 0
            if rev < (INT_MIN) // 10 or (rev == (INT_MIN) // 10 and pop < -1*(abs(INT_MIN)%10)):
                return 0

            rev = rev * 10 + pop

        return rev * sign

# T = log10(X)
# S = 1