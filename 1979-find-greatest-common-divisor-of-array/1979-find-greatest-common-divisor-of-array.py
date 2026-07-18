class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        return gcd(a,b)
    def gcd(a,b)->int:
        while(b!=0):
            temp=b
            b=a%b
            a=temp
        return a if (b==0) else 0 