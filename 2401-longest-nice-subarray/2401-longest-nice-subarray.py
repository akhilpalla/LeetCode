class Solution:
    def longestNiceSubarray(self, nums):
        n, max_len, left, val = len(nums), 0, 0, 0

        for right in range(n):
            while val&nums[right] > 0:
                val = val^nums[left]
                left += 1 

            val = val^nums[right]

            max_len = max(max_len,right-left+1)
                
        return max_len