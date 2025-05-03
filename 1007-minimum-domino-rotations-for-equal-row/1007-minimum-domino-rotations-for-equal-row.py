class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def countDifference(A, B, num):
            countA, countB = 0, 0
            
            for i in range(len(A)):
                if A[i] != num and B[i] != num:
                    return -1
                else:
                    if A[i] != num: countA+=1
                    if B[i] != num: countB+=1
    
            return min(countA, countB)
        
        if A.count(A[0]) + B.count(A[0]) < len(A) and A.count(B[0]) + B.count(B[0]) < len(A):
            return -1
        
        res1 = countDifference(A, B, A[0])
        res2 = countDifference(A, B, B[0])
        
        if min(res1, res2) > 0: return min(res1, res2)
        return max(res1, res2)