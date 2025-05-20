class Solution:
    def isZeroArray(self, nums, queries):
        pre = [0] * (len(nums) + 1)

        for query in queries:
            pre[query[0]] += 1
            if query[1] + 1 < len(pre):
                pre[query[1] + 1] -= 1

        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]

        for i in range(len(nums)):
            if pre[i] < nums[i]:
                return False

        return True