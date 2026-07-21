class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count_ones = 0
        cons_zero_counts = [0, 0]
        max_two_cons_zeros = 0
        zero_streak = False

        for c in s:
            if c == "1":
                count_ones += 1
                zero_streak = False
                if cons_zero_counts[0] > 0:
                    max_two_cons_zeros = max(max_two_cons_zeros, cons_zero_counts[0] + cons_zero_counts[1])
            else:
                if zero_streak:
                    cons_zero_counts[1] += 1
                else:
                    cons_zero_counts[0] = cons_zero_counts[1]
                    cons_zero_counts[1] = 1
                    zero_streak = True

        if zero_streak and cons_zero_counts[0] > 0:
            max_two_cons_zeros = max(max_two_cons_zeros, cons_zero_counts[0] + cons_zero_counts[1])

        return count_ones + max_two_cons_zeros