class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] < mid :
                start = mid + 1
            else:
                end = mid - 1
        
        if start < len(arr) and arr[start] == start:
            return start
        
        return -1