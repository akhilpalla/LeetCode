from typing import List
from collections import deque
import sys
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append([flight[1], flight[2]])
        
        q = deque()
        q.append([0, [src, 0]]) #<stops,node,dist>
        dist = [sys.maxsize] * n
        dist[src] = 0
        
        while len(q) != 0:
            stops, temp = q.popleft()
            node, cost = temp
            
            if stops > k:
                continue
            
            for neigh in adj[node]:
                adjN, edW = neigh
                
                if cost + edW < dist[adjN] and stops <= k:
                    dist[adjN] = cost + edW
                    q.append([stops + 1, [adjN, cost + edW]])
        
        if dist[dst] == sys.maxsize:
            return -1
        
        return dist[dst]

# T = E
# S = E + V (adjList , PQ , distArray) 