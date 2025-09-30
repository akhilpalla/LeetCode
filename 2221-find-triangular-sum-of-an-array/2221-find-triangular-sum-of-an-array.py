class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        temp=[]
        while len(nums)>1:
            for k in range(len(nums)-1):
                s=nums[k]+nums[k+1]
                if s<10:
                    nums[k]=s
                else:
                    nums[k]=(nums[k]+nums[k+1])%10
            nums.pop()
        return nums[0]