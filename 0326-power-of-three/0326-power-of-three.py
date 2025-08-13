class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        low, high = 0, 19  # 3^0 to 3^19
        while low <= high:
            mid = (low + high) // 2
            val = 3**mid
            if val == n:
                return True
            elif val < n:
                low = mid + 1
            else:
                high = mid - 1
        return False
