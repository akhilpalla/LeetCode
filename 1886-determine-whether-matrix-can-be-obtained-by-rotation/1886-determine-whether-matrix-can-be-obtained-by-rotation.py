class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if mat == target: return True
        mat.reverse()                           
        mat = [list(x) for x in zip(*mat)]       
        if mat == target: return True
        mat.reverse()
        mat = [list(x) for x in zip(*mat)]
        if mat == target: return True
        mat.reverse()
        mat = [list(x) for x in zip(*mat)]
        return mat == target