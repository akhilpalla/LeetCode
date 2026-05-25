class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] != '0':
            return False
        if '1' * maxJump in s:
            return False
        queue = deque([0])
        max_visited = 0 
        while queue:
            curr = queue.popleft()
            if curr + minJump <= n - 1 <= curr + maxJump:
                return True
            start_window = curr + minJump
            end_window = min(curr + maxJump, n - 1)
            start_search = max(start_window, max_visited + 1)
            for j in range(start_search, end_window + 1):
                if s[j] == '0':
                    queue.append(j)
            max_visited = max(max_visited, end_window)
        return False