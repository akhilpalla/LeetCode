class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        max_num = max(nums)
        
        spf = list(range(max_num + 1))
        for i in range(2, int(max_num**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def prime_score(x):
            factors = set()
            while x != 1:
                factors.add(spf[x])
                x //= spf[x]
            return len(factors)
        
        prime_scores = [prime_score(num) for num in nums]
        
        left = [-1] * n
        right = [n] * n
        stack = []
        
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        elements = sorted([(nums[i], i) for i in range(n)], reverse=True)
        
        score = 1
        for value, i in elements:
            count = (i - left[i]) * (right[i] - i)
            if count <= k:
                score = (score * pow(value, count, MOD)) % MOD
                k -= count
            else:
                score = (score * pow(value, k, MOD)) % MOD
                break
        
        return score