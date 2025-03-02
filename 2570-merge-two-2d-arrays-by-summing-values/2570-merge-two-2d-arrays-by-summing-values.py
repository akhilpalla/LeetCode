class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        return sorted(list(l) for l in (Counter(dict(nums1)) + Counter(dict(nums2))).items())