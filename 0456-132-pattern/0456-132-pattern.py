class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: 
            return False

        # Initialize the third number of the 132 pattern
        third = float('-inf')
        stack = []

        # Iterate the numbers from right to left
        for num in reversed(nums):
            # If we find a number smaller than the third one, return True
            if num < third: 
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)

        return False