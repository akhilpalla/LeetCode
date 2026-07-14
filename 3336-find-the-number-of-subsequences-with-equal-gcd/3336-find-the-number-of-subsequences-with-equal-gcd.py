class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def recur(i, gcd1, gcd2):
            if i >= len(nums):
                if gcd1 == gcd2 and gcd1 != 0:
                    return 1
                return 0
            pick1 = recur(i+1, gcd(gcd1, nums[i]), gcd2)
            pick2 = recur(i+1, gcd1, gcd(gcd2, nums[i]))
            notPick = recur(i+1, gcd1, gcd2)
            return pick1 + pick2 + notPick
        return recur(0, 0, 0) % MOD