class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        c = dict()
        ans = list()
        for i, num in enumerate(nums):
            c[num] = c.get(num, 0) + 1
            if i >= k - 1:
                ans.append(sum(num * count for num, count in sorted(c.items(), key = lambda x:[-x[1], -x[0]])[:x]))
                c[nums[i - k + 1]] -= 1
        return ans