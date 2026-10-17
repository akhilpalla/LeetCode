class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_digits(num):
            s = 0
            a = num
            while num:
                s += num % 10
                num //= 10
            return (s, a)
        ans = len(nums)
        idx_arr = {a: i for i, a in enumerate(sorted(nums, key = sum_digits))}
        s = set()
        for i, num in enumerate(nums):
            j = idx_arr[num]
            if j not in s:
                while j not in s:
                    s.add(j)
                    j = idx_arr[nums[j]]
                ans -= 1
        return ans