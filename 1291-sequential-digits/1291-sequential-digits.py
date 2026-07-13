class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        digits_low = len(str(low))
        digits_high = len(str(high))
        superset = "123456789"
        for i in range(digits_low, digits_high + 1):
            for j in range(0, 9 - i + 1):
                sub_string = superset[j:j + i]
                num = int(sub_string)
                if low <= num <= high:
                    ans.append(num)
        return ans