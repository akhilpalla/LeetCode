class Solution:
    def minTimeToReach(self, mt: List[List[int]]) -> int:
        vis = set()
        mt[0][0] = -1
        q = [(0,0,0)]
        while q:
            pts,i,j = heapq.heappop(q)
            if (i,j) in vis:
                continue
            vis.add((i,j))
            if i<0 or j<0 or i>=len(mt) or j>=len(mt[0]):
                continue
            pts = max(pts,mt[i][j]+1)
            if i==len(mt)-1 and j==len(mt[0])-1:
                return pts

            heapq.heappush(q,(pts+1,i+1,j))
            heapq.heappush(q,(pts+1,i,j+1))
            heapq.heappush(q,(pts+1,i-1,j))
            heapq.heappush(q,(pts+1,i,j-1))
        return -1