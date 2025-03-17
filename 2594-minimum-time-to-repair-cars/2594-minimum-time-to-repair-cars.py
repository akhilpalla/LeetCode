class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars**2
        while left < right:
            mid = (right + left) // 2
            total_cars = 0
            for rank in ranks:
                total_cars += isqrt(mid//rank)
                if total_cars >= cars:
                    break
            if total_cars >= cars:
                right = mid
            else:
                left = mid + 1
            
        return left