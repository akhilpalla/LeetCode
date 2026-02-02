from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedList()
        n = len(nums)
        res = nums[0]
        for i,val in enumerate(nums[1:dist+2]):
            sl.add((val,i+1))
        cursum = 0
        for i in range(k-1):
            cursum += sl[i][0]
        res += cursum
        for i in range(2,n-dist):
            j = sl.bisect_left((nums[i-1], i-1))
            if j < k-1:
                cursum -= sl[j][0]
                sl.pop(j)
                sl.add((nums[i+dist],i+dist))
                j = sl.bisect_left((nums[i+dist],i+dist))
                if j < k-1:
                    cursum += nums[i+dist]
                else:
                    cursum += sl[k-2][0]
            else:
                sl.add((nums[i+dist],i+dist))
                j = sl.bisect_left((nums[i+dist],i+dist))
                if j < k-1:
                    cursum += nums[i+dist] - sl[k-1][0]
                sl.remove((nums[i-1],i-1))
            res = min(res, nums[0] + cursum)
        return res