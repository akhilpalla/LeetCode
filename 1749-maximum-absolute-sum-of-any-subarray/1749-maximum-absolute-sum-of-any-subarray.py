class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        pref_min = 0
        pref_max = 0
        ans = 0
        for num in nums:
            prefix += num
            current = prefix - (pref_min if prefix > 0 else pref_max)
            if current > ans:
                ans = current
            elif -current > ans:
                ans = -current
            if prefix < pref_min:
                pref_min = prefix
            elif prefix > pref_max:
                pref_max = prefix
        return ans        