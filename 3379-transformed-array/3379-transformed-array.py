class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = list()
        org_len = len(nums)
        nums = nums + nums + nums
        for i in range(org_len, org_len * 2):
            result.append(nums[(nums[i] + i)%len(nums)])
        return result