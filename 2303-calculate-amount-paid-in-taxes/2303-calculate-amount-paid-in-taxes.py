class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0.0
        last_bound = 0
        for bound, percent in brackets:
            if income <= 0: return ans
            ans += (min(bound - last_bound, income) * percent) / 100
            income -= (bound - last_bound)
            last_bound = bound
        return ans