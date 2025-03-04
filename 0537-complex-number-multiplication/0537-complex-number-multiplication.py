class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        k=num1[:-1].split('+')
        k2=num2[:-1].split('+')
        print(k,k2)
        f=int(k[0])*int(k2[0])-int(k2[1])*int(k[1])
        z=int(k[0])*int(k2[1])+int(k[1])*int(k2[0])
        return str(f)+"+"+str(z)+'i'