class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = float('inf')
        high = float('-inf')
        totalArea = 0
        
        for x, y, l in squares:
            low = min(low, y)
            high = max(high, y + l)
            totalArea += l * l

        
        eps = 1e-5
        while high - low > eps:
            mid = (low + high) / 2.0
            lowerArea = 0
            
            for x, y, l in squares:
                lowerLength = calculateLowerLength(mid, y, l)
                lowerArea += lowerLength * l
            
            if lowerArea < totalArea / 2.0:
                low = mid
            else:
                high = mid
        
        return (low + high) / 2.0

def calculateLowerLength(mid: float, y: int, l: int) -> float:
    if mid <= y:
        return 0
    elif mid >= y + l:
        return l
    else:
        return mid - y