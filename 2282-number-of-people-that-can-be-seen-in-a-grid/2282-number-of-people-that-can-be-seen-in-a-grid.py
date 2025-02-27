class Solution:
    def seePeople(self, mat: List[List[int]]) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])

        grid = [[0] * m for _ in range(n)]

        for i in range(n):
            stack = []
            for j in range(m-1, -1, -1):
                count = 0
                while stack and stack[-1] < mat[i][j]:
                    stack.pop()
                    count += 1
                count += bool(stack)
                if not stack or stack[-1] > mat[i][j]:
                    stack.append(mat[i][j])
                grid[i][j] = count

        for j in range(m):
            stack = []
            for i in range(n-1, -1, -1):
                count = 0
                while stack and stack[-1] < mat[i][j]:
                    stack.pop()
                    count += 1
                count += bool(stack)
                if not stack or stack[-1] > mat[i][j]:
                    stack.append(mat[i][j])
                grid[i][j] += count

        return grid