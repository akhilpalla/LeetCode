class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        freq_map = {}
        L=[""]*len(s)
        for i in range(len(s)):
            try:
                freq_map[s[i]]+=1
            except:
                freq_map[s[i]]=1
        freq_map = sorted([[char,freq] for char,freq in freq_map.items()], key=lambda x:x[1],reverse=True)
        if(k<=1):
            return s
        last_used = {}
        for i in range(len(s)):
            flag = False
            for j in range(len(freq_map)):
                frequency = freq_map[j][1]
                ch = freq_map[j][0]
                if(frequency==0):
                    continue
                if(ch not in last_used or i-last_used[ch]>=k):
                    L[i]=ch
                    freq_map[j][1]-=1
                    last_used[ch]=i
                    flag = True
                    break
            if(flag==False):
                return ""
            freq_map.sort(key=lambda x:x[1],reverse=True)
        return "".join(L)