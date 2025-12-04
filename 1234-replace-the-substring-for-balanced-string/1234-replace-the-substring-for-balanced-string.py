class Solution:
    def balancedString(self, s):
        n = len(s)
        k = n // 4
        count = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            count[char] += 1
        def is_valid(counts, target):
            return all(v <= target for v in counts.values())
        if is_valid(count, k):
            return 0
        min_len = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left <= right and is_valid(count, k):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
        return min_len