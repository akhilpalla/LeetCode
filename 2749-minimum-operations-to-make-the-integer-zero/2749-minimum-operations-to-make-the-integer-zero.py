class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return bin(num1).count('1')
        op = 0
        while bin(num1).count('1') > op:
            op += 1
            num1 -= num2
            if num1 < op:
                return -1
        return op