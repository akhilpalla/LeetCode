class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:


        def valid(string : str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')' :
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()
            
            if valid(curr):
                result.append(curr)
                found = True
            
            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue
                
                nxt = curr[:i] + curr[i+1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result