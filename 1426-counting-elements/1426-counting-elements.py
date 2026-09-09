class Solution:
    def countElements(self, arr: List[int]) -> int:
        exist = 1002 * [False]
        for n in arr:
            exist[n] = True
        out = 0
        for n in arr:
            if exist[n+1]:
                out+=1
        return out