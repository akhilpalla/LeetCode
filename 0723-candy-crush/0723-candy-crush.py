class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        def crash():
            crash_set = set()
            # horizontal
            visited = set()
            for r, c in product(range(m), range(n)):
                if (r,c) in visited or board[r][c] == 0:
                    continue
                i, j = c,c
                while i-1 > 0 and board[r][i-1] == board[r][i]:
                    i -= 1
                while j+1 < n and board[r][j] == board[r][j+1]:
                    j += 1
                if j-i+1 < 3:
                    continue
                for k in range(i,j+1):
                    visited.add((r,k))
                    crash_set.add((r,k))
            # vertical
            visited = set()
            for r, c in product(range(m), range(n)):
                if (r,c) in visited or board[r][c] == 0:
                    continue
                i, j = r,r
                while i-1 > 0 and board[i-1][c] == board[i][c]:
                    i -= 1
                while j+1 < m and board[j][c] == board[j+1][c]:
                    j += 1
                if j-i +1 < 3:
                    continue
                for k in range(i,j+1):
                    visited.add((k, c))
                    crash_set.add((k, c))
            if not crash_set:
                return False
            for r, c in crash_set:
                board[r][c] = 0

            return True

        def drop():
            for c in range(n):
                i = m-1
                while board[i][c] != 0 and i > 0:
                    i -= 1
                j = i - 1
                while j >= 0:
                    if board[j][c] == 0:
                        j -= 1
                    else:
                        board[i][c], board[j][c] = board[j][c], 0
                        i -= 1
                        j -= 1

            pass
        
        def print_board():
            for row in board:
                print("".join(["{0:5}".format(x) for x in row]))
        
        count = 0
        while crash():
            drop()
        return board
        