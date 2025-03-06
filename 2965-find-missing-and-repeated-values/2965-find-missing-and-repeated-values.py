class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        g = [j for i in grid for j in i]
        ans = []

        ans.append(sum(g) - sum(set(g)))
        ans.append(sum(range(1, max(g)+1)) - sum(set(g)))
        if ans[1] == 0:
            ans[1] = max(g)+1

        return ans