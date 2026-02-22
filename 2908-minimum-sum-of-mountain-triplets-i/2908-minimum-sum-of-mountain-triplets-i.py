class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        minn=sum(nums)*sum(nums)
        new=minn

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if minn > nums[i] + nums[j] + nums[k] and (nums[i] < nums[j] and nums[k] < nums[j]):
                        minn =  nums[i] + nums[j] + nums[k]
        if minn==new:
            return -1
        else:
            return minn