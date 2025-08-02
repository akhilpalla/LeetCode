class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c = collections.Counter()
        _min = float('inf')
        for elem in basket1:
            c[elem] += 1
            _min = min(_min, elem)
        for elem in basket2:
            c[elem] -= 1
            _min = min(_min, elem)
        arr = []
        for key in c:
            if c[key] % 2 != 0:
                return -1
            arr += ([key] * abs(c[key] // 2))
        arr.sort()
        res = 0
        for i in range(len(arr) // 2):
            res += min(2 * _min, arr[i])
        return res