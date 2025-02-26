class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for x, y in dominoes:
            key = (min(x, y), max(x, y))
            count[key] += 1
        return sum(v * (v - 1) // 2 for v in count.values())