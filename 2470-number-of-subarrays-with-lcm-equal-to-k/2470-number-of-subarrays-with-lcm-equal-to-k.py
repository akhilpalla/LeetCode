class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            #cur = [i]
            a = nums[i]
            for j in range(i, len(nums)):
                a = lcm(a, nums[j])
                if a == k:
                    res += 1
        return res