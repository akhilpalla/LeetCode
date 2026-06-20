class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort(key=lambda x: x[0] + x[1])
        answer = 0
        best_building, best_height = 1, 0
        for building, limit in restrictions:
            left = best_building - best_height
            right = min(
                2 * n - best_building + best_height,
                building + limit
            )
            answer = max(answer, (right - left) // 2)
            if building - limit > left:
                best_building = building
                best_height = limit
        answer = max(
            answer,
            n - best_building + best_height
        )
        return answer