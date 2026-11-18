class Solution:
    def minChanges(self, s: str) -> int:
    
        changes = 0
        i = 0
        if "1" in s and "0" in s :
            while i < len(s) :
                if s[i] != s[i+1]:
                    changes += 1
                i += 2 
            return changes        
            
        else :
            return 0
        