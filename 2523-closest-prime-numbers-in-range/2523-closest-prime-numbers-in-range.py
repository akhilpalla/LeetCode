class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        visited, primes = [False] * (right + 1), []
        for i in range(2, right + 1):
            if visited[i] == False: primes.append(i)
            for p in primes:
                if i * p > right: break
                visited[i * p] = True
                if i % p == 0: break
        idx = 0
        while idx < len(primes) and primes[idx] < left: idx += 1
        if idx >= len(primes) - 1: return [-1, -1]
        ans = [primes[idx], primes[idx + 1]]
        idx += 1
        while idx < len(primes) - 1:
            if primes[idx + 1] - primes[idx] < ans[1] - ans[0]:
                ans = [primes[idx], primes[idx + 1]]
            idx += 1
        return ans