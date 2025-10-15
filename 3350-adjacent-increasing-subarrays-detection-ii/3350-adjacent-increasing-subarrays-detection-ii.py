class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        cnt = 1
        precnt = 0
        ans = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt = cnt
                cnt = 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans