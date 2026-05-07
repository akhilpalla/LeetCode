class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        suffix = [inf]
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(min(suffix[-1], nums[i]))
        suffix = (suffix[::-1])
        ans = [0] * len(nums)
        mx = 0
        for i in range(len(nums)):
            mx = max(mx, nums[i])
            if mx <= suffix[i + 1]:
                ans[i] = mx
        el = 0
        for i in range(len(nums) - 1, -1, -1):
            if ans[i] != 0:
                el = ans[i]
            ans[i] = el
        return (ans)