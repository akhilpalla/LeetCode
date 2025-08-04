#This problem can be converted to --> max length of subarray with at most 2 types of numbers

#Brute: Generate all the subarrays --> N^2 and S --> 1

#Better: sliding window 2 pointer using while --> T = 2N ||| S = 1
"""
class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        l = r = lenn = maxLen = 0
        n = len(arr)
        hashh = {}

        while(r<n):
            if arr[r] not in hashh:
                hashh[arr[r]] = 1
            else:
                hashh[arr[r]]+=1

            if (len(hashh) > 2):
                while(len(hashh)>2):
                    hashh[arr[l]]-=1
                    if hashh[arr[l]] == 0:
                        hashh.pop(arr[l])

                    l+=1

            lenn = r-l+1
            maxLen = max(maxLen , lenn)
            r+=1
        
        return maxLen
"""
#Optimal: sliding window 2 pointer using if --> T = N ||| S = 1
class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        l = r = lenn = maxLen = 0
        n = len(arr)
        hashh = {}

        while(r<n):
            if arr[r] not in hashh:
                hashh[arr[r]] = 1
            else:
                hashh[arr[r]]+=1

            if (len(hashh) > 2):
                if(len(hashh)>2):
                    hashh[arr[l]]-=1
                    if hashh[arr[l]] == 0:
                        hashh.pop(arr[l])

                    l+=1

            lenn = r-l+1
            maxLen = max(maxLen , lenn)
            r+=1
        
        return maxLen
        