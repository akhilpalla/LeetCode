class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums)==3:
            return sum(nums)
        m1 = nums[0]
        m2=m3=math.inf
        for n in nums[1:]:
            if n<m2:
                m2,m3=n,m2
            elif n<m3:
                m3=n
        return m1+m2+m3