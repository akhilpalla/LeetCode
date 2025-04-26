class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minPos = maxPos = invalidPos = -1
        
        for i, num in enumerate(nums):
            if not (minK <= num <= maxK):
                invalidPos = i
            if num == minK:
                minPos = i
            if num == maxK:
                maxPos = i

            validStart = min(minPos, maxPos)
            if validStart > invalidPos:
                count += validStart - invalidPos
        
        return count