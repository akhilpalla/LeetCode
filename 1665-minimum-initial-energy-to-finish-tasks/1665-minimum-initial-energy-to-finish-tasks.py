class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[0]-x[1])
        l = 0 
        r = 0
        for a, m in tasks:
            r = max(a, m, r)
        r *= len(tasks)
        def is_valid(e):
            for a, m in tasks:
                if e < m:
                    return False
                if e < a:
                    return False
                e -=a
            return True
        while l <= r:
            mid = l + (r-l)//2
            if is_valid(mid):
                r = mid-1
            else:
                l = mid +1
        return l