class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x1=0
        for a in arr1:
            x1^=a
        x2=0
        for b in arr2:
            x2^=b
        return x1&x2