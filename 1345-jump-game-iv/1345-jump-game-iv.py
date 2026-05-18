class Solution:
    def minJumps(self, arr: List[int]) -> int:
        edges, n = defaultdict(list), len(arr)
        for i in range(n):
            edges[arr[i]].append(i)
        queue, visited, steps = deque([0]), set([0]), 0
        while queue:
            for _ in range(len(queue)):
                idx = queue.popleft()
                if idx == n-1:
                    return steps
                for new_idx in [idx-1, idx+1] + edges.pop(arr[idx], []):
                    if 0 <= new_idx < n and new_idx not in visited:
                        if new_idx == n-1:
                            return steps + 1
                        queue.append(new_idx)
                        visited.add(new_idx)
            steps += 1