class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        changes = 0
        isOdd = True if nums[0] % 2 == 1 else False
        ones = 1 if nums[0] % 2 == 1 else 0
        zeroes = 1 if nums[0] % 2 == 0 else 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                zeroes += 1
                if isOdd:
                    isOdd = False
                    changes += 1
            else:
                ones += 1
                if not isOdd:
                    isOdd = True
                    changes += 1
        
        return max(changes + 1, ones, zeroes)