class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev='1'
        for i in s:
            if i=='1' and prev=='0':
                return False
            prev=i
        return True 