class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        seen = {}
        def find_path(row, col, current_health):
            if current_health <= seen.get((row, col), -1):
                return False
            seen[(row, col)] = current_health
            new_health = current_health
            if grid[row][col] == 1:
                new_health -= 1
            if new_health <= 0:
                return False
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            for row_delta, col_delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                new_row = row + row_delta
                new_col = col + col_delta
                if new_row < 0 or new_row >= len(grid):
                    continue
                if new_col < 0 or new_col >= len(grid[0]):
                    continue
                if find_path(new_row, new_col, new_health):
                    return True
            return False
        return find_path(0, 0, health)