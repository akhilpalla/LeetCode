class Solution:
    def countAndSay(self, n: int) -> str:
        
        ans1='1'
        ans2='11'
        if(n==1):
            return ans1
        if(n==2):
            return ans2
        ans=ans2
        for i in range(2,n):
            temp=""
            count=1
            var=ans[0]
            for j in range(1,len(ans)):
                if(ans[j]==ans[j-1]):
                    count+=1
                    var=ans[j]
                    continue
                if(ans[j]!=ans[j-1]):
    #                 print("hi")
                    temp=temp+str(count)+var
                    count=1
                    var=ans[j]
                    continue
            temp=temp+str(count)+var

            ans=temp
    #         print(ans)
        return ans
        
        
        