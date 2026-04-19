class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return False   
        n1=n2=float('inf')
        for j in nums:
            if j<=n1:
                n1=j
            elif j<=n2:
                n2=j
            else:
                return True
        return False