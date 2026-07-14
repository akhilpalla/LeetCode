from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        for k,v in d.items():
            if v==1:
                return k
        return -1