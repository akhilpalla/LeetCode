class Solution(object):
    def minElement(self, nums):
        result = []
        for num in nums:
            temp = 0
            for digit in str(num):
                temp += int(digit)
            result.append(temp)
        return min(result)