class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = []

        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i]:
                ans.append(nums[i])
        
        return ans + [0] * (n-len(ans))