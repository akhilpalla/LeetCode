class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        range_sum = [0 for _ in range(N)]
        range_sum[0] = nums[0]
        for i in range(1, N):
            range_sum[i] = nums[i] + range_sum[i-1]

        def getRangeSum(l, r):
            if l == 0:
                return range_sum[r]
            
            return range_sum[r] - range_sum[l-1]

        ans = 0
        for i, num in enumerate(nums):
            if num >= k:
                continue

            if getRangeSum(0, i) * (i+1) < k:
                ans += (i+1)
                continue

            ok = i
            ng = 0
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if getRangeSum(mid ,i) * (i - mid + 1) < k:
                    ok = mid
                else:
                    ng = mid

            ans += (i - ok + 1)                    

        return ans            