class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        max_val = None
        count=0
        if a>b:
            max_val=a
        else:
            max_val=a
        if a!=b:
            for i in range(1,max_val):
                if a%i==0:
                    if b%i==0:
                        count+=1

            return count
        else:
            for i in range(1,max_val+1):
                if a%i==0:
                    if b%i==0:
                        count+=1

            return count