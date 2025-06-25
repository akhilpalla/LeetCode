class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1.sort()
        nums2.sort()
        
        def findRank(product: int) -> int:
            ans = 0
            
            for num1 in nums1:
                if num1 == 0:
                    if product >= 0: ans += len(nums2)
                    continue
                if num1 < 0:
                    ans += len(nums2) - bisect_left(nums2, ceil(product / num1))
                else:
                    ans += bisect_right(nums2, product // num1)
            return ans

        l, r = -int(1e10), int(1e10)
        while l < r:
            mid = l + (r - l) // 2
            if findRank(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return r