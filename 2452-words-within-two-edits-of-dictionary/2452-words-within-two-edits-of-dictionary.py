class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        sz = len(queries[0])
        for q in queries:
            for d in dictionary:
                diff = 0
                for i in range(sz):
                    if q[i] != d[i]:
                        diff += 1          
                    if diff > 2:
                        break              
                if diff <= 2:
                    ans.append(q)
                    break              
        return ans