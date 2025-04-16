class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        ans = 0
        numPairs = 0
        l = 0
        r = 0
        counts = {}

        while r < len(nums):
            numPairs += counts.get(nums[r], 0)
            counts[nums[r]] = counts.get(nums[r], 0) + 1

            while numPairs >= k:
                ans += len(nums) - r
                counts[nums[l]] -= 1
                numPairs -= counts[nums[l]]
                l += 1
            r += 1
        
        return ans