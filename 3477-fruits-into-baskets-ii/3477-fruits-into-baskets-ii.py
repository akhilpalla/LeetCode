class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        tmp = [-1] * n

        for i in range(n):
            for j in range(0, n):
                if fruits[i] <= baskets[j] and tmp[j] == -1:
                    tmp[j] = 1
                    break

        return sum(1 for i in tmp if i == -1)