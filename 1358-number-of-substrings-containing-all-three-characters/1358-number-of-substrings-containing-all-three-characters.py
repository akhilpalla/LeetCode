# Brute: Generate all the substrings
"""
cnt = 0
for i in range(n):
    hash={}
    for j in range(i,n):
        hash[s[j] - ord(a)] = 1
        if hash[0]+hash[1]+hash[2] == 3:
            cnt+=1
T = N^2
S = 1
"""
#Better: once we have the string which has all the 3 chars we can stop iterating because even after adding we will have all 3 chars --> so add the length
"""
cnt = 0
for i in range(n):
    hash={}
    for j in range(i,n):
        hash[s[j] - ord(a)] = 1
        if hash[0]+hash[1]+hash[2] == 3:
            cnt+=(n-j)
            break
T = N^2
S = 1
"""
#Optimal: Using 2 pointer and sliding window

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        count = 0
        
        mp = {'a': 0, 'b': 0, 'c': 0}
        
        while j < n:
            mp[s[j]] += 1
            
            while mp['a'] >= 1 and mp['b'] >= 1 and mp['c'] >= 1:
                count += (n - j)
                mp[s[i]] -= 1
                i += 1
            
            j += 1
        
        return count

# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:

#         lastSeen = {}
#         cnt = 0
#         for i in range(len(s)):
            
#             lastSeen[s[i]]=i
            
#             if( ("a" in lastSeen) and ("b" in lastSeen) and ("c" in lastSeen)):
#                 cnt = cnt + (1 + min(lastSeen['a'] , lastSeen['b'] , lastSeen['c']))

#         return cnt


        