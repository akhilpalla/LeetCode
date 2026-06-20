class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[]
        l.append(0)
        for i in range(len(gain)):
            l.append(gain[i]+l[-1])
        return max(l)