class Solution:

    def isGood(self, nums):
        n = len(nums)
        mp = {}

        for i in range(1,n):
            mp[i] = mp.get(i,0) + 1

        mp[n-1] = mp.get(n-1,0) + 1

        for x in nums:
            if mp.get(x,0) > 0:
                mp[x] -= 1
            else:
                return False
        return True