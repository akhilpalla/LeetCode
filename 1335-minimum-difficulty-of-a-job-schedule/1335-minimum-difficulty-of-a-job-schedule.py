class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n<d:
            return -1
        nexHardest = [0]*n
        nexHardest[n-1] = jobDifficulty[n-1]
        for i in range(n-2,-1,-1):
            nexHardest[i] = max(nexHardest[i+1],jobDifficulty[i])
        
        @lru_cache(None)
        def dp(i,day):
            nonlocal n
            if day==d:
                return nexHardest[i]
            temp = float('inf')
            hardest = jobDifficulty[i]
            for j in range(i,n-(d-day)):
                hardest = max(jobDifficulty[j], hardest)
                temp = min(temp, hardest+dp(j+1,day+1))
            return temp
        return dp(0, 1)