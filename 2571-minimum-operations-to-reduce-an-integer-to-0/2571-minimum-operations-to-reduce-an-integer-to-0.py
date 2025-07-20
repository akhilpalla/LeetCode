class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        q = deque([(0, n)])
        optimizer_set = set()
        optimizer_set.add(n)
        
        ref = []
        power = 1
        while power <= 2 * n:
            ref.append(power)
            power *= 2
        
        while q:
            level, node = q.popleft()
            
            if node == 0:
                return level
            
            for p in ref:
                next_node = node - p
                if next_node >= 0 and next_node not in optimizer_set:
                    optimizer_set.add(next_node)
                    q.append((level + 1, next_node))
                
                next_node = node + p
                if next_node <= 2 * n and next_node not in optimizer_set:
                    optimizer_set.add(next_node)
                    q.append((level + 1, next_node))

        return -1
