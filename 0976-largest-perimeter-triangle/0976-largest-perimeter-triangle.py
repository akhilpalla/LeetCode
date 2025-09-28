class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            a, b, c = nums[i], nums[i-1], nums[i-2]
            if b + c > a:
                return a + b + c
        return 0