class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums) - 1
        right, left = Counter(nums), {}
        
        for i in range(n):
            left[nums[i]] = left.get(nums[i], 0) + 1
            right[nums[i]] -= 1

            if ((i + 1) < left[nums[i]] * 2) and ((n - i) < right[nums[i]] * 2):
                return i

        return -1