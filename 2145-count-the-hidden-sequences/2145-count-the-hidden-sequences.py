class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0
        min_prefix = 0
        max_prefix = 0
        
        for diff in differences:
            curr += diff
            min_prefix = min(min_prefix, curr)
            max_prefix = max(max_prefix, curr)
        
        return max(0, (upper - max_prefix) - (lower - min_prefix) + 1)
        