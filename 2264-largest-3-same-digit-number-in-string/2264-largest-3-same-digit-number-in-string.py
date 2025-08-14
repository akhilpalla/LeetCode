class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, ans = 0, ''
        for r in range(len(num)):
            if num[r] != num[l]:
                l = r
            elif r - l == 2 and ans < num[r]:
                ans = num[r]
        return ans * 3