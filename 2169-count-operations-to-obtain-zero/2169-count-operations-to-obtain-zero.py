class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ct=0
        while True:
            if(num1==0 or num2==0):
                return ct
            elif(num1>=num2):
                num1-=num2
            else:
                num2-=num1
            ct+=1