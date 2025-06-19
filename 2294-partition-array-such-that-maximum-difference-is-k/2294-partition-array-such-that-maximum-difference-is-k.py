class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        # Base Case
        if nums[-1] - nums[0] <= k:
            return 1

        ans = []
        ans.append(nums[0])
        res = []
        for i in range(len(nums)-1):
            if nums[i + 1] - ans[0] <= k:
                ans.append(nums[i + 1])
            else:
                res.append(ans)
                ans = []
                ans.append(nums[i + 1])
        res.append(ans)
        return len(res)