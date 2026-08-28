class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        S=s;T=target
        cnt=Counter(S)
        odds=''.join(c for c in cnt if cnt[c]&1)
        if len(odds)>1: return ''
        for c in cnt: cnt[c]//=2
        res=''
        def bt(i,cur,tight):
            nonlocal res
            if i==len(S)//2:
                cand=cur+odds+cur[::-1]
                if cand>T: res=cand
                return
            for c in sorted(cnt):
                if cnt[c]==0: continue
                if tight and c<T[i]: continue
                cnt[c]-=1
                bt(i+1,cur+c,tight and c==T[i])
                cnt[c]+=1
                if res!='': return
        bt(0,'',True)
        return res