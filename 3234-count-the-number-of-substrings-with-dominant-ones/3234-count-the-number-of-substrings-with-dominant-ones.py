class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr=[0]*len(s)
        Sum=0
        for i in range(len(s)):
            if s[i]=='1':
                Sum=Sum+1
            arr[i]=Sum
        Sum,i,j,f=0,0,0,-1
        while i<len(s):
            if s[i]=='1' and i>f:
                q=i
                while q<len(s):
                    if s[q]=='1':
                        q=q+1
                    else:
                        break
                Sum=Sum+(q-i)*(q-i+1)//2
                f=q
            if i<f:
                j=f
            else:
                j=i
            while j<len(s):
                ones=arr[j]-arr[i]+int(s[i])
                zeros=(j-i+1)-ones
                if ones>zeros**2:
                    diff=int(math.sqrt(ones))-zeros
                    if j+diff>len(s):
                        Sum=Sum+len(s)-j
                        j=len(s)
                    elif diff==0:
                        Sum=Sum+1
                        j=j+1
                    else:
                        Sum=Sum+diff
                        j=j+diff
                elif ones==zeros**2:
                    Sum=Sum+1
                    j=j+1
                else:
                    diff=zeros**2-ones
                    j=j+diff
            i=i+1
        return Sum