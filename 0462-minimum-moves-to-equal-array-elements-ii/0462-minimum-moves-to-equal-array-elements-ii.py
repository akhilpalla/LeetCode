class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        make = nums[n//2]
        ans = 0
        for i in nums :
            ans += abs(make-i)
        return ans
 