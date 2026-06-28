class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()   
        current = 0
        for i in range(len(arr)):   
            if arr[i] > current:  
                current += 1
        return current