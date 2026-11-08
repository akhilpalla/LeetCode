from collections import Counter

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = Counter()
        cols = Counter()

        computers = set()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    computers.add((r, c))

                    rows[r] += 1
                    cols[c] += 1

        answer = 0
        for r, c in computers:
            if rows[r] > 1 or cols[c] > 1:
                answer += 1
        
        return answer
                    