class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter=Counter(nums)
        if max(counter.values())==1:return 0
        operations=0
        rem=len(nums)%3
        div=(len(nums)//3)
        for i in range(0,len(nums)-rem,3):
            if max(counter.values())==1:return operations
            else:
                counter[nums[i]]-=1
                counter[nums[i+1]]-=1
                counter[nums[i+2]]-=1
                operations+=1
        if operations==div and max(counter.values())>1:
            operations+=1
        return operations
