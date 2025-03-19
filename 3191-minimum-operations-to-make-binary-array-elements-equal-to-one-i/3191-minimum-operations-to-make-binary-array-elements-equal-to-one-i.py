class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                count += 1
                nums[i] = 1
                nums[i+1] = 0 if nums[i+1] == 1 else 1
                nums[i+2] = 0 if nums[i+2] == 1 else 1
        if nums[-2] != 1 or nums[-1] != 1:
            return -1
        return count