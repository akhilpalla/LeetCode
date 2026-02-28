class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaryString = ""  
        for i in range(1,n+1):
            binaryString += str(bin(i))[2:]
        decimal = int(binaryString, 2)
        return decimal % 1000000007