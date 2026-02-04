class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        dp = []
        res = -inf
        for i,a in enumerate(nums):
            if i == 0:
                dp = [[a,-inf,-inf,-inf]]
                continue
            lastdp = [a for a in dp[-1]]
            newdp = [a,-inf,-inf,-inf]
            if nums[i] > nums[i-1]:
                newdp[1] = max(lastdp[1]+a,lastdp[0]+a)
                newdp[3] = max(lastdp[3]+a,lastdp[2]+a)
            elif nums[i] < nums[i-1]:
                newdp[2] = max(lastdp[2]+a,lastdp[1]+a)
            res = max(res,newdp[3])
            dp.append(newdp)
        return res