class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def check(threshold):
            ans = 0
            idx = 1
            while idx < n:
                if nums[idx] - nums[idx - 1] <= threshold:
                    ans += 1
                    idx += 2
                else:
                    idx += 1
            return ans

        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if check(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left