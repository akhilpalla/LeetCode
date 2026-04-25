class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def to1d(point:List[int]):
            if point[1]==0: 
                return point[0]
            elif point[0]==side:  
                return side+point[1]
            elif point[1]==side:  
                return 3*side-point[0]
            else:  
                return 4*side-point[1]
        arr = list(map(to1d,points))
        arr.sort()  
        def check(minDist):
            n = len(arr)
            startOfSecond = bisect.bisect_left(arr, arr[0] + minDist)
            if n - startOfSecond < k - 1:
                return False
            for i in range(startOfSecond):
                count = 1
                curPt = arr[i]
                for _ in range(k - 1):
                    j = bisect.bisect_left(arr, curPt + minDist)
                    if j>=n:
                        break
                    distFromEnd = (4 * side - arr[j])
                    clockwiseDist =  distFromEnd + arr[i]
                    if clockwiseDist < minDist:
                        break
                    curPt = arr[j]
                    count += 1
                if count == k:
                    return True
            return False  
        left,right,ans = 1,side,1  
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans