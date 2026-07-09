class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        for i in range(1, n):
            if nums[i - 1] + maxDiff >= nums[i]:
                parent[i] = parent[i - 1]
        return [parent[x] == parent[y] for x, y in queries]