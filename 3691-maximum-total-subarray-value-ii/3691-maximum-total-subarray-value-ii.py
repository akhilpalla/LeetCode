class SegmentTree:
    def __init__(self, arr, func):
        self.n = len(arr)
        self.arr = arr
        self.identity = -math.inf if func == max else math.inf
        self.func = func
        self.tree = [self.identity] * (self.n * 4)
        self._build(0, 0, self.n-1)
    def _build(self, ind, low, high):
        if low >= high:
            self.tree[ind] = self.arr[low]
            return 
        mid = (low + high) // 2
        self._build(ind*2+1, low, mid)
        self._build(ind*2+2, mid+1, high)
        self.tree[ind] = self.func(self.tree[ind*2+1], self.tree[ind*2+2])
    def _query(self, ind, low, high, left, right):
        if left <= low and high <= right:
            return self.tree[ind]
        if right < low or high < left:
            return self.identity
        mid = (low + high) // 2
        leftResult = self._query(ind*2+1, low, mid, left, right)
        rightResult = self._query(ind*2+2, mid+1, high, left, right)
        return self.func(leftResult, rightResult)
    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxST = SegmentTree(nums, max)
        minST = SegmentTree(nums, min)
        score = 0
        L, R = 0 ,len(nums) - 1
        maxHeap = [(-(maxST.query(L, R) - minST.query(L,R)), L, R)]
        seen = {(L, R)}
        for _ in range(k):
            s, L, R = heapq.heappop(maxHeap)
            score += -s
            if L+1 <= R and (L+1, R) not in seen:
                seen.add((L+1, R))
                ns = maxST.query(L+1, R) - minST.query(L+1, R)
                heapq.heappush(maxHeap,(-ns, L+1, R))
            if L <= R-1 and (L, R-1) not in seen:
                seen.add((L, R-1))
                ns = maxST.query(L, R-1) - minST.query(L, R-1)
                heapq.heappush(maxHeap, (-ns, L, R-1))
        return score 