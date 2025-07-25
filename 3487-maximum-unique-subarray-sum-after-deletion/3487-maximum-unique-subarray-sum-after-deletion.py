class Solution:
    def maxSum(self, nums: List[int]) -> int:
        valSet = set()
        maxVal = -inf
        for val in nums:
            maxVal = max(val, maxVal)
            if val > 0:
                valSet.add(val)
        
        if len(valSet) == 0:
            return maxVal
        return sum(valSet)