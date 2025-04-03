class Solution:
    def maximumTripletValue(self, a: List[int]) -> int:
        return max(max((v-u)*w for v,u,w in zip(accumulate(a,max),a[1:],[*accumulate(a[:1:-1],max)][::-1])),0)