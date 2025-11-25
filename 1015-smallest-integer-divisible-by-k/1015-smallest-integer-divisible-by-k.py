class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 1
        cnt = 1
        seen = set()
        if remainder % k == 0:
            return 1
        for i in range(k + 1):
            cnt += 1
            if remainder in seen: return -1
            seen.add(remainder)
            remainder = (remainder * 10 + 1) % k
            print(remainder)
            if remainder == 0:
                return cnt