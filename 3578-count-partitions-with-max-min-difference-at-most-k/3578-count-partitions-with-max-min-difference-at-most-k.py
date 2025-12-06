class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7
        sl = SortedList()
        dp = [0] * (N + 1)
        dpp = [0] * (N + 2)
        dp[0] = 1
        dpp[1] = 1
        q = deque()
        for i in range(N):
            while len(sl) > 0 and (abs(sl[0] - nums[i]) > k or abs(sl[-1] - nums[i]) > k):
                j = q.popleft()
                sl.remove(nums[j])
            q.append(i)
            sl.add(nums[i])
            j = q[0]
            dp[i + 1] = dpp[i + 1] - dpp[j]
            dp[i + 1] %= MOD
            dpp[i + 2] = dp[i + 1] + dpp[i + 1]
            dpp[i + 2] %= MOD
        return dp[N]