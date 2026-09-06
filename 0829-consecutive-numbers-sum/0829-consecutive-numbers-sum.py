class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = floor(math.sqrt(2*n))
        for i in range(1,k+1):
            if (2*n)%i==0 and (2*n/i+i)%2!=0:
                count +=1
                
        return count