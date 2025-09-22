class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ctr = Counter(nums)                              
        mx = max(ctr.values())                           
        return sum(filter(lambda x: x == mx, ctr.values()))  