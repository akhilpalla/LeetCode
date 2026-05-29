class Solution:
    def confusingNumber(self, N: int) -> bool:
        mapping ={0:0, 1:1, 6:9, 8:8, 9:6}
        digit = []
        for n in (str(N)):
            if int(n) not in mapping:
                return False
            digit.append(int(n))
        rotate = [mapping[n] for n in digit][::-1]
        return digit != rotate