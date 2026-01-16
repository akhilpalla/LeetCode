class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 1_000_000_007
        vFences.append(1)
        vFences.append(n)
        hFences.append(1)
        hFences.append(m)
        
        vDists = set([abs(vFences[i]-vFences[j]) for i in range(len(vFences)) for j in range(i)])
                
        maxSide = -1
        for i in range(len(hFences)):
            for j in range(i):
                side = abs(hFences[i]-hFences[j])
                if side > maxSide and side in vDists:
                    maxSide = side
        return -1 if maxSide == -1 else (maxSide**2 % MOD)
                