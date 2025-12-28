class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count  = 0
        cols = len(grid[0])
        for row in grid:
            left, right = 0 , cols - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] < 0: 
                    count += right - mid + 1
                    right = mid - 1
                else: left = mid + 1
        return count