class Solution:
    def replaceNonCoprimes(self, nums):
        stack = []
        for num in nums:
            while stack and gcd(num,stack[-1]) >= 2:
                num = lcm(num,stack[-1])
                stack.pop()
            stack.append(num)
        return stack