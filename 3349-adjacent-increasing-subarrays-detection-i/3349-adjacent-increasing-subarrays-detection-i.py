class Solution:        
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def isIncreasing(idx):
            prev = float('-inf')
            for i in range(idx, idx + k):
                if nums[i] <= prev:
                    return False
                prev = nums[i]
            return True
        for i in range(len(nums) - 2 * k + 1):
            if isIncreasing(i) and isIncreasing(i + k): 
                return True
        return False