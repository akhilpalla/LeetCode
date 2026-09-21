class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [[0 for l in range(len(nums))] for i in range(k)] 
        dp[nums[0] % k ][0] = 1
        to_way = [[] for i in range(k)]
        for i in range(k):
            for j in range(k):
                to_way[j].append((i*j)%k) 
        for i in range(1, len(nums)):
            l = nums[i] % k
            dp[l][i] += 1
            for j, z in enumerate(to_way[l]):
                dp[z][i] += dp[j][i-1]
        return [sum(v) for v in dp]
        