class Solution:
    def countPartitions(self, a: List[int]) -> int:
        q = sum(a)
        return sum((2*p-q)%2==0 for p in accumulate(a[:-1]))