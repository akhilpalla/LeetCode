class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        mod = 10**9+7
        for i, (li, ri, ki, vi) in enumerate(queries):
            idx = li
            while idx <= ri:
                nums[idx] = ( nums[idx] * vi ) % mod
                idx += ki
        
        res = nums[0]
        for i in range(1, n):
            res ^= nums[i]
        
        return res