class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        m = mass
        last = asteroids[-1]
        for a in asteroids:
            if m < a:
                return False
            if m > last:   
                return True
            m += a
        return True