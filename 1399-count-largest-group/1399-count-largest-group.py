class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0] * (9 * 4 + 1)
        for i in range(1, n + 1):
            count[self.getDigitSum(i)] += 1
        max_count = max(count)
        return count.count(max_count)

    def getDigitSum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum