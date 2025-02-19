class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = 10001
        sums = [0] * n

        for num in nums:
            sums[num] += num

        prev, curr = 0, sums[1]

        for i in range(2, n):
            prev, curr = curr, max(prev + sums[i], curr)

        return curr