class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list1=[[]]
        n=len(nums)
        for i in range(1,2**n):
            list2=[]
            for j in range(n):
                if (i&1<<j):
                    list2.append(nums[j])
                list2.sort()
                if list2 not in list1:
                    list1.append(list2)
        return list1