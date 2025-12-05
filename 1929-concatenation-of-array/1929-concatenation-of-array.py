class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [nums[i%n]for i in range(2*n)]
        return ans
        