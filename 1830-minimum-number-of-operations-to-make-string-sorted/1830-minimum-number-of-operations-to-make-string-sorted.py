class Solution:
    @lru_cache(None)
    def compute_factorial(self, num):
        if num <= 1:
            return 1
        return (num * self.compute_factorial(num - 1)) % (10**9 + 7)

    def makeStringSorted(self, s: str) -> int:
        mod_value = 10**9 + 7
        length = len(s)
        total_ops = 0
        char_count = [0] * 26

        for idx in range(length - 1, -1, -1):
            char_pos = ord(s[idx]) - ord('a')
            char_count[char_pos] += 1
            prefix_sum = sum(char_count[:char_pos]) * self.compute_factorial(length - idx - 1)
            
            for count in char_count:
                prefix_sum = (prefix_sum * pow(self.compute_factorial(count), mod_value - 2, mod_value)) % mod_value
                
            total_ops = (total_ops + prefix_sum) % mod_value
        
        return total_ops