class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        freq = [0] * (m + 1)
        for cost in costs:
            freq[cost] += 1
        op = 0
        for cost in range(m + 1):
            for _ in range(freq[cost]):
                if coins - cost >= 0:
                    op += 1
                    coins -= cost
        return op