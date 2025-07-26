class Solution:
    def maxSubarrays(self, n: int, A: List[List[int]]) -> int:
        
        right = [[] for _ in range(n + 1)]
        
        for a, b in A:
            right[max(a, b)].append(min(a, b))
        
        res = 0
        cur, prev = 0, 0
        imp = [0] * (n + 1)
        
        for r in range(1, n + 1):
            for l in right[r]:
                if l > cur:
                    prev = cur
                    cur = l
                elif l > prev:
                    prev = l
            
            res += r - cur
            imp[cur] += cur - prev

        return res + max(imp)