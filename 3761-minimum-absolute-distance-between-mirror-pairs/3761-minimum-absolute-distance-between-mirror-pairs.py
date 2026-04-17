class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        dp = {}
        mini = float("inf")
        for i in range(len(nums)):
            string = str(nums[i])
            if string in dp:
                mini = min(mini,i-dp[string])
            j = len(string)-1
            while i >= 0:
                if string[j] != "0":
                    break
                j -= 1
            string = string[:j+1]
            dp[string[::-1]] = i
        return -1 if mini == float("inf") else mini