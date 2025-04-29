class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = count = 0
        m, d = max(nums), {}
        for i, j in enumerate(nums):
            if j == m:
                count += 1
                d[count] = i
            if count >= k:
                v = count - k + 1
                ans += (d[v] + 1)
        return ans