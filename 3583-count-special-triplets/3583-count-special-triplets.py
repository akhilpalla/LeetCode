class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left={}
        right={}
        mod=10**9 + 7
        for i in nums:
            right[i]=1+right.get(i,0)
        res=0
        for i in nums:
            right[i]-=1
            res=(res+left.get(i*2,0)*right.get(i*2,0))%mod
            left[i]=1+left.get(i,0)
        return res