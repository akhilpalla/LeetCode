class Solution:
    def findMin(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        ans = arr[0]  # Initialize with the first element

        while low <= high:
            mid = (low + high) // 2

            # Update `ans` with the minimum found so far
            ans = min(ans, arr[mid])

            # If the left part is sorted
            if arr[low] <= arr[mid]:
                # The minimum must be in the left part (or `arr[mid]`)
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                # The right part is sorted, so the minimum must be in the right part
                ans = min(ans, arr[mid])
                high = mid - 1

        return ans

