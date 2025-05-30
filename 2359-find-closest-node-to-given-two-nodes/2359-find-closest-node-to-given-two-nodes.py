class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        path1 , path2 = set(),set()
        ans = n+1
        path1.add(node1)
        path2.add(node2)
        
        while node1 >= 0 or node2 >= 0:
            if node1 in path2:   
                ans = min(ans,node1)
            if node2 in path1: 
                ans = min(ans,node2)
            if ans != n+1:
                return ans

            if node1 >= 0:
                node1 = edges[node1] 
                if node1 in path1: 
                    node1 = -1
                if node1 >= 0 :
                    path1.add(node1)
            if node2 >= 0:
                node2 = edges[node2]
                if node2 in path2:
                    node2 = -1
                if node2 >= 0:
                    path2.add(node2)
        
        return -1