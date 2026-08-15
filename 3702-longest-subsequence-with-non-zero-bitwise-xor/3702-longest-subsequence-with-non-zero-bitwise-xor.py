class Solution:
    def longestSubsequence(self, A):
        return (lambda s,n,x: 0 if s == {0} else n if x else n-1)(set(A), len(A), reduce(xor, A))           