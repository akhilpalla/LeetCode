#Book Allocation
#Painters Partition
#Split Array Largest Sum
class Solution:

    def countStudents(self,arr, pages):
        n = len(arr)   
        students = 1
        pagesStudent = 0
        for i in range(n):
            if pagesStudent + arr[i] <= pages:
                pagesStudent += arr[i]
            else:
                students += 1
                pagesStudent = arr[i]
        return students

    def splitArray(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m > n:
            return -1

        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(arr, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low
            