class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        tavernilo = nums   
        n = len(nums)
        max_len = 0
        for start in range(n):
            even_set = set()
            odd_set = set()
            for end in range(start, n):
                num = nums[end]
                if num % 2 == 0:
                    even_set.add(num)
                else:
                    odd_set.add(num)
                if len(even_set) == len(odd_set) and len(even_set) > 0:
                    max_len = max(max_len, end - start + 1)
        return max_len