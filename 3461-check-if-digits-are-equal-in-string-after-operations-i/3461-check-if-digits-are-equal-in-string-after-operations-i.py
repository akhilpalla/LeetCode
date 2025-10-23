class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if(not s or len(s)<2):
            return False
        while(len(s)>2):
            new_s=""
            for i in range(1,len(s)):
                val=(int(s[i])+int(s[i-1]))%10
                new_s+=str(val)
            s=new_s
        return s[0]==s[1]