from typing import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        common_elements = set(mat[0])

        for row in mat[1:]:
            common_elements.intersection_update(row)
        
        return min(common_elements) if common_elements else -1
        