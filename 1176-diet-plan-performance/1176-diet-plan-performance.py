class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        l = 0
        r = l + k
        rolling_calories = sum(calories[:k])
        points = 1 if rolling_calories > upper else -1 if rolling_calories < lower else 0
        while r < len(calories):
            rolling_calories = (rolling_calories - calories[l] + calories[r])
            points += 1 if rolling_calories > upper else -1 if rolling_calories < lower else 0
            l += 1
            r += 1
        return points