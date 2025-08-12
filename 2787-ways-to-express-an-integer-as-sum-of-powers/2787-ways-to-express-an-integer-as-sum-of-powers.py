from math import pow, floor
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        numFloor = math.ceil(pow(n, 1/x)) + 1
        modVal = pow(10, 9) + 7
        nums = []
        for i in range(1, numFloor):
            nums.append(int(pow(i, x)))
        memo = [[-1] * len(nums) for _ in range(n+1)]
        def dp(index, target):
            if target == 0:
                return 1
            if target < 0 or index >= len(nums):
                return 0
            
            if memo[target][index] == -1:

                useDigit = 0
                if nums[index] <= target:
                    useDigit = dp(index + 1, target - nums[index])
                dontUseDigit = dp(index + 1, target)
                memo[target][index] = useDigit + dontUseDigit
            return memo[target][index]
        dp(0, n)
        return int(memo[n][0] % modVal)