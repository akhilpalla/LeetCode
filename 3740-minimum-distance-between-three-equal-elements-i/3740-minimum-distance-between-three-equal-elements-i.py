class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        d=defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
        
        res = float('inf')
        
        for l in d.values():
            if len(l) < 3:
                continue
            
            for j in range(len(l) - 2):
                a, b, c = l[j], l[j+1], l[j+2]
                dist = abs(a - b) + abs(b - c) + abs(c - a)
                res = min(res, dist)
        
        return res if res != float('inf') else -1




class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        
        res = float('inf')

        # Manual binary search function
        def lower_bound(arr, target):
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        for val, arr in d.items():
            if len(arr) < 3:
                continue

            # simulate the process for each index
            for idx in arr:
                pos = lower_bound(arr, idx)
                # check around that position manually
                for j in range(max(0, pos - 2), min(len(arr) - 3, pos) + 1):
                    a, b, c = arr[j], arr[j + 1], arr[j + 2]
                    dist = 2 * (c - a)
                    res = min(res, dist)

        return res if res != float('inf') else -1


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        last = defaultdict(list)
        res = float('inf')

        for i, val in enumerate(nums):
            last[val].append(i)
            
            # keep only last 3 occurrences
            if len(last[val]) > 3:
                last[val].pop(0)
            
            if len(last[val]) == 3:
                a, b, c = last[val]
                dist = 2 * (c - a)
                res = min(res, dist)

        return res if res != float('inf') else -1


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        res = float('inf')
        pos = defaultdict(deque)  # store indices for each number (up to 3)

        for r in range(n):
            val = nums[r]
            pos[val].append(r)

            # keep only last 3 indices for that number
            if len(pos[val]) > 3:
                pos[val].popleft()

            # check if we have a valid good tuple
            if len(pos[val]) == 3:
                a, b, c = pos[val]
                dist = 2 * (c - a)
                res = min(res, dist)

            # move left pointer logically (not strictly needed)
            while l <= r and len(pos[nums[l]]) > 3:
                pos[nums[l]].popleft()
                l += 1

        return res if res != float('inf') else -1