class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num2count = {}

        for num in nums:
            if num in num2count:
                num2count[num] += 1
            else:
                num2count[num] = 1
        
        num2count = {k:v for k, v in num2count.items() if v == 1}

        if len(num2count) == 0:
            return -1
        else:
            return max(num2count)