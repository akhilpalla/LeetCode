class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right, result = 0, sum(nums), []
        
        for i in nums:
            right -= i
            result.append(abs(left-right))
            left += i

        return result