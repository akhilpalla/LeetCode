class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        def get_score(ind):
            res=energy[ind]
            pref=res
            i=ind-k
            while(i>=0):
                pref+=energy[i]
                res=max(res,pref)
                i-=k
            return res
        res=float("-inf")
        for i in range(k):
            res=max(res,get_score(len(energy)-1-i))
        return res