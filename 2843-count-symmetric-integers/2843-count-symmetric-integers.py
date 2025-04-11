class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        nums = []
        for i in range(low,high+1):
            str_num = str(i)
            if len(str_num)%2!=0:
                pass
            else:
                a = len(str_num)//2
                num1 = str_num[:a]
                num2 = str_num[a:]

                n1 = sum(int(digit) for digit in num1)
                n2 = sum(int(digit) for digit in num2)

                if n1==n2:
                    nums.append(i)

        return len(nums)