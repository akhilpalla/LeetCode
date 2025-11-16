class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for first in range(len(nums) - 2):
            second = first + 1
            third = len(nums) - 1
            while second <= third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < target:
                    res += abs(second - third)
                    second += 1
                else:
                    third -= 1
        return res