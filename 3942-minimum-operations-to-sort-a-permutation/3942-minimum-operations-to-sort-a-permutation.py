class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count_breaks = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count_breaks += 1
        if count_breaks == 0:  
            return 0
        min_idx = nums.index(0) 
        if count_breaks == 1:  
            ans = min_idx  
            ans = min(ans, 2 + n - ans)  
            return ans
        if n - count_breaks == 1:  
            ans = n - min_idx  
            ans = min(ans, min_idx + 2)  
            return ans
        return -1