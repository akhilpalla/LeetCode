class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, n, res, mp, curr = 0, len(nums), 0, defaultdict(int), 0
        for r in range(n):
            curr += nums[r]
            mp[nums[r]] += 1 
            while r - l + 1 > len(mp):
                mp[nums[l]] -= 1 
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                curr -= nums[l]
                l += 1 
            res = max(res, curr)
        return res 