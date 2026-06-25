class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        cnt = 0
        for i, num in enumerate(nums):
            if num == target:
                cnt += 2
            pref[i + 1] = i - cnt + 1
        ans = 0
        arr = SortedList()
        for i, p in enumerate(pref):
            ans += i - arr.bisect_right(p)
            arr.add(p)
        return ans