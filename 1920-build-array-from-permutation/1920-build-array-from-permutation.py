class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            val=nums[nums[i]]
            ans.append(val)
        return ans