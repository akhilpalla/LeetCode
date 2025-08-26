class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for length, width in dimensions:
            d = length * length + width * width  # squared diagonal
            if d > max_diagonal:
                max_diagonal = d
                max_area = length * width
            elif d == max_diagonal:
                if max_area <= length * width:
                    max_area = length * width
        return max_area