class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s='0'
        for i in range(1,n):
            r=''
            for i in s:
                if i=='0':
                    r+='1'
                else:
                    r+='0'
            s=s+'1'+r[::-1]
        return s[k-1]