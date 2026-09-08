class Node:
    next={}
    pre=0
    end=0
    f=0
    def __init__(self):
        self.next={}
        self.pre=0
        self.end=0
        self.f=0

    def __str__(self):
        return f'{self.pre},{self.end},{self.f},{self.next}' 

class Trie:
    root=None
    def __init__(self):
        self.root=Node()

    def insert(self,s):
        temp=self.root
        i=0
        while(i<len(s)):
            if(temp.next.get(s[i],None)==None):
                temp.next[s[i]]=Node()
            temp.pre+=1
            temp=temp.next[s[i]]
            i+=1
        temp.end+=1

    def check(self,temp,s,i,k):
        if(i==len(s)):
            if(temp.end+temp.pre>=k):
                temp.f=max(temp.f,1)
                return 1
            return 0
        if(temp.pre+temp.end>=k):
            t=1+self.check(temp.next[s[i]],s,i+1,k)
            temp.f=max(temp.f,t)
        return temp.f
    
    def search(self,s,k):
        d=0
        temp=self.root
        ans=0
        i=0
        while(i<=len(s)):
            if(temp.pre+temp.end<k):break
            if(i==len(s)):
                if(temp.pre+temp.end-1>=k):
                    ans=max(ans,d-1+temp.f)
                break
            for a,b in temp.next.items():
                cnt=temp.next[a].pre+temp.next[a].end
                if(a!=s[i] and cnt>=k):
                    ans=max(d+temp.next[a].f,ans)
                elif(a==s[i] and cnt-1>=k):
                    ans=max(d+1,ans)
            temp=temp.next[s[i]]
            i+=1
            d+=1
        return ans
class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        t=Trie()
        for s in words:
            t.insert(s)
            t.check(t.root,s,0,k)
        ans=[0 for i in range(len(words))]
        for i in range(len(words)):
            ans[i]=t.search(words[i],k)
        return ans