class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, stack = 0, [0]
        for num in nums:
            while num < stack[~0]: stack.pop()
            res+= (num != stack[~0])
            stack.append(num)
        return res