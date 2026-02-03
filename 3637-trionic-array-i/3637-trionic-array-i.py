class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        left = 0
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                left = i
                break
        if left == 0: return False
        right = n - 1
        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                right = i
                break
        if right == n - 1: return False
        for i in range(left, right):
            if nums[i] <= nums[i + 1]:
                return False
        return True