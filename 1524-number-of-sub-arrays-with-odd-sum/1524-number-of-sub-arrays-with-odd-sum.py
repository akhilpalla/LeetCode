class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        preSum = [0, A[0]]
        for i in range(1,n):
            preSum.append(preSum[-1] + A[i])
        
        even = 0
        odd = 0
        
        for i in preSum:
            if i%2 == 0:
                even += 1
            else:
                odd += 1
                
        return (odd*even)%mod