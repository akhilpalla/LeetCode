class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cache = defaultdict(list)
        for s, v in items:
            heappush(cache[s], -v)
        ans = []
        for k, vals in cache.items():
            cur = 0
            for _ in range(5):
                cur += -heappop(cache[k])
            ans.append([k, cur // 5])
        return sorted(ans, key=lambda x: x[0])