class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=c=0
        m,n=100,len(blocks)
        for j in range(n):
            if blocks[j]=='W':
                c+=1
            if j-i==k-1:
                m=min(m,c)
                if blocks[i]=='W':
                    c-=1
                i+=1                
        return m