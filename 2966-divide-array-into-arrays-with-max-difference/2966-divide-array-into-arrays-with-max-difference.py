class Solution:
    def divideArray(self, a: List[int], k: int) -> List[List[int]]:
        return [a.sort(),r:=[a[i:i+3] for i in range(0,len(a),3)],r*all(q-p<=k for p,_,q in r)][2]