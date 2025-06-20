class Solution:
    def solveQueries(self, nums: List[int], qs: List[int]) -> List[int]:
        n=len(nums)
        
        f=defaultdict(list)
        for i,num in enumerate(nums):
            f[num].append(i)

        def helper(q):
            if q>=n:return -1
            num=nums[q]
            arr=f[num]
            nn=len(arr)
            if nn==1:return -1
            ind=bisect_left(arr,q)
            prev=arr[(ind-1+nn)%nn]
            next=arr[(ind+1)%nn]
            if prev>q:prev-=n
            if next<q:next+=n
            left=q-prev
            right=next-q
            return min(left,right)
        
        res=[helper(q) for q in qs]

        return res