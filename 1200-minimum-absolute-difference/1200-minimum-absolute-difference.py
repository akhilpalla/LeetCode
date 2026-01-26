class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        min_diff = float('inf')
        ans = []
        for i in range(n - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])
        for i in range(n - 1):
            if arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans