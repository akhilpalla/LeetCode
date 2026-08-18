class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        res = -1
        if k==1:
            temp_max = -1
            for k, v in d.items():
                if v==1 and k > temp_max:
                    temp_max = k
            res = temp_max
        elif k==len(nums):
            temp_max = -1
            for num in nums:
                if num > temp_max:
                    temp_max = num
            res = temp_max
        else:
            first_num = -1
            last_num = -1
            if d[nums[0]] == 1:
                first_num = nums[0]
            if d[nums[-1]] == 1:
                last_num = nums[-1]
            res = max(first_num, last_num)
        return res