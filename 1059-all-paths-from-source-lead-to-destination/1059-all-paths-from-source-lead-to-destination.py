from enum import Enum, auto

class Status(Enum):
    ON_STACK = auto(),
    VISITED = auto()

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        al = defaultdict(list)
        for a, b in edges:
            al[a].append(b)
        
        if destination in al:
            return False
        
        visited = {}
        stack = [source]
        while stack:
            v1 = stack[-1]
            if v1 in visited:
                visited[v1] = Status.VISITED
                stack.pop()
            else:
                visited[v1] = Status.ON_STACK
                if v1 not in al and v1 != destination:
                    return False
                for v2 in al[v1]:
                    if v2 in visited:
                        if visited[v2] == Status.ON_STACK:
                            return False
                    else:
                        stack.append(v2)
        return True