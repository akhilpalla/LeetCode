class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        j=m-1
        dp = [0 for i in range(n+1)]  
        q=n-1
        for i in range(n-1,-1,-1):
            if(i!=n-1):
                dp[i]=dp[i+1]
            if(j>=0 and word1[i]==word2[j]):
                dp[i]+=1
                j-=1
        ans=[]
        found= False
        i=0
        j=0
        k=m
        while(i<n and j<m):
            if word1[i]==word2[j]:
                ans.append(i)
                i+=1
                j+=1
                k-=1
            else:
                if k-1<=dp[i+1] and found==False:
                    ans.append(i)
                    i+=1
                    j+=1
                    k-=1
                    found=True
                else:
                    i+=1
        if(len(ans) == m):
            return ans
        else:
            return []