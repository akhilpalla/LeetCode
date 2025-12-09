class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        product_sum = sum(a * b for a, b in zip(nums1, nums2))
        return product_sum