class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign(k):
            t = sorted(tasks[:k])  
            w = SortedList(workers[-k:])   
            p = pills
            
            for i in reversed(range(k)):
                task = t[i]
                if w and w[-1] >= task:
                    w.pop()  
                else:
                    idx = w.bisect_left(task - strength)
                    if idx == len(w) or p == 0:
                        return False
                    w.pop(idx)
                    p -= 1
            return True

        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
            