class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Compute absolute distances
        distance1 = abs(x - z)
        distance2 = abs(y - z)
        
        # Compare distances
        if distance1 == distance2:
            return 0
        return 1 if distance1 < distance2 else 2