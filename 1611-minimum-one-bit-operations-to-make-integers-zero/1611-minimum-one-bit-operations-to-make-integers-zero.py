class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        b=bin(n)[2:]
        x=len(b)
        ans=0
        flag=True
        for i in range(x):
            k=x-1-i #index from right
            if b[i]=='1':
                term=2**(k+1)-1
                if flag:
                    ans +=term
                else:
                    ans-=term
                flag=not(flag)
        return(ans)