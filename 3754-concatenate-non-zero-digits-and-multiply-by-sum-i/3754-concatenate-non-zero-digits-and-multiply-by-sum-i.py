class Solution:
    def sumAndMultiply(self, n: int) -> int:
        total=sum(int(k) for k in str(n))
        res=str(n).replace("0","")
        if res=="":
            return 0
        return int(res)*total
        