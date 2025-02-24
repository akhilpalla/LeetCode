# Brute: Generate all the subarrays --> N^2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maxLen = 0
        lenn = 0
        zeros = 0
        n = len(nums)

        while(r<n):
            if(nums[r] == 0):
                zeros+=1
            if(zeros>1):
                if(nums[l] == 0):
                    zeros-=1
                l+=1
            if(zeros<=1):
                lenn = r-l+1
                maxLen = max(lenn,maxLen)
            
            r+=1
        return maxLen