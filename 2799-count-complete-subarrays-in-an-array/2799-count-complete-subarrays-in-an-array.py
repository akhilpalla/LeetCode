class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        validLen = len(set(nums))
        res = 0
        freq = Counter()  

        l = 0
        for r in range(n):
            freq[nums[r]] += 1

            while len(freq) == validLen:
                res += (n - r)
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1    

        return res