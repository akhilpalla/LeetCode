class Solution:
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0] * n
        mx = nums[0]
        prefixGcd[0] = nums[0]
        for i in range(1, n):
            mx = max(mx, nums[i])
            prefixGcd[i] = math.gcd(mx, nums[i])
        prefixGcd.sort()
        i, j = 0, n - 1
        ans = 0
        while i < j:
            ans += math.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        return ans