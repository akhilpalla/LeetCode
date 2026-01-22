class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        c = 0
        while nums != sorted(nums):
            msum, mid = float('inf'), 0
            for i in range(len(nums) - 1):
                if msum > nums[i] + nums[i + 1]:
                    msum = nums[i] + nums[i + 1]
                    mid = i
            nums = nums[:mid] + [msum] + nums[mid + 2:]
            c += 1
        return c