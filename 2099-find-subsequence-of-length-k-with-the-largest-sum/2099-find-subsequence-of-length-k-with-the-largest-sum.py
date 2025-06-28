class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top, ans = Counter(sorted(nums, reverse=True)[:k]), []
        for n in nums:
            if n in top and top[n]: ans, top[n] = ans+[n], top[n]-1
            if len(ans) == k: return ans 