class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1_sum, n1_zeroes = sum(nums1), nums1.count(0)
        n2_sum, n2_zeroes = sum(nums2), nums2.count(0)
        n1_minsum, n2_minsum = n1_sum + n1_zeroes, n2_sum + n2_zeroes
        if (not n1_zeroes and n1_minsum < n2_minsum) or (not n2_zeroes and n2_minsum < n1_minsum):
            return -1
        return max(n1_minsum, n2_minsum)