class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=max(nums)
        for num in nums:
            c+=abs(num-m)
        return c
        