# Brute: generate all the substring 

# OPtimal: 2pointer and sliding window 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l=0
        r=0
        hashh={}
        maxLen=0

        while(r<n):
            if(s[r] in hashh):
                # It ensures that we only update l when the repeated character is actually within our current window.
                if(l <= hashh[s[r]]):
                    l = hashh[s[r]] + 1
                    lenn = r-l+1
                    maxLen = max(maxLen , lenn)
                    hashh[s[r]] = r
            
            lenn = r-l+1
            maxLen = max(maxLen , lenn)
            hashh[s[r]] = r
            r+=1

        return maxLen


        