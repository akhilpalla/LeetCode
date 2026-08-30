class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        a = nums.index(min(nums))
        b = nums.index(max(nums))
        left = min(a, b)
        right = max(a, b)
        case1 = right + 1
        case2 = n - left
        case3 = (left + 1) + (n - right)
        return min(case1, case2, case3)