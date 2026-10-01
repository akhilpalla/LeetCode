class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], fixed_express_cost: int) -> List[int]:
        n = len(regular)
        dp_regular, dp_express = [float("inf")] * (n + 1), [float("inf")] * (n + 1)
        dp_regular[0] = 0
        dp_express[0] = fixed_express_cost
        optimal_costs = []
        for i in range(n):
            regular_cost, express_cost = regular[i], express[i]
            dp_regular[i + 1] = min(regular_cost + dp_regular[i], regular_cost + dp_express[i])
            dp_express[i + 1] = min(fixed_express_cost + express_cost + dp_regular[i], express_cost + dp_express[i])
            optimal_costs.append(min(dp_regular[i + 1], dp_express[i + 1]))
        return optimal_costs