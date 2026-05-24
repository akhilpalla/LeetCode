class Solution(object):
    def maximumValueSum(self, board):
        rows = len(board)
        cols = len(board[0])
        arr = []
        for i in range(rows):
            pq = []
            for j in range(cols):
                heapq.heappush(pq, (board[i][j], i, j))
                if len(pq) > 3:
                    heapq.heappop(pq)
            while pq:
                arr.append(heapq.heappop(pq))
        arr.sort(reverse=True, key=lambda x: x[0])   
        ans = float('-inf')
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i][1] == arr[j][1]:   
                    continue
                for k in range(j + 1, len(arr)):
                    if arr[i][1] == arr[k][1] or arr[j][1] == arr[k][1] or arr[i][2] == arr[j][2] or arr[j][2] == arr[k][2] or arr[i][2] == arr[k][2]:
                        continue
                    current_sum = arr[i][0] + arr[j][0] + arr[k][0]
                    ans = max(ans, current_sum)
                    break   
        return ans