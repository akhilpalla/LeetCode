class Solution:
    def recursion(self,s1,n,idx,target,dp):
        
        if s1 == target: return 0
        if idx == n: return float('inf')
        
        if s1 in dp:return dp[s1]
        
        best = float('inf')
        
        if s1[idx]==target[idx]:best = self.recursion(s1,n,idx+1,target,dp)
        
        else:
            for i in range(idx+1,n):
            
                if s1[i] != target[idx]:continue
            
                new  = s1[:idx] + s1[i] + s1[idx+1:i] + s1[idx] + s1[i+1:]
            
                tmp = self.recursion(new,n,idx+1,target,dp) + 1
                if tmp < best: best = tmp
        
        dp[s1] = best       
        
        return best
   
    def kSimilarity(self, s1: str, s2: str) -> int:
        
        dp = {}
        return self.recursion(s1,len(s1),0,s2,dp)