class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        costs = [i+1 for i in aliceArrows]

        N = len(costs)
        
        def _recursion(index, arr, remaining):
            if index == N:
                return arr
            
            answer1 = _recursion(index + 1, arr + [0], remaining)
            if remaining >= costs[index]:
                answer2 = _recursion(index + 1, arr + [costs[index]], remaining - costs[index])
            else:
                answer2 = []
            
            return max(answer1, answer2, key=lambda x: sum([i for i, v in enumerate(x) if v > 0]))
        
        ret = _recursion(0, [], numArrows)

        if sum(ret) < numArrows:
            ret[0] += numArrows - sum(ret)
        
        return ret