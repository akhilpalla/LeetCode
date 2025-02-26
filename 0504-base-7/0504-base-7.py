class Solution:
    def convertToBase7(self, num: int) -> str:
        temp = -num if num < 0 else num
        res = ''
        while temp:
            res = str(temp % 7) + res
            temp //= 7
        if num < 0: res = '-' + res
        return res if res else '0'