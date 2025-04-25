class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + (nums[i] % modulo == k)
        
        count = 0
        lookup = defaultdict(int)

        for x in pref:
            count += lookup[((x - k) % modulo)]
            lookup[(x % modulo)] += 1


        return count