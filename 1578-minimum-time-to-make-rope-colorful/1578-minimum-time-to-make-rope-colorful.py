class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        res =  0
        min_time = 0
        for b, t in zip(colors,neededTime):
            if stack and b == stack[-1][0]:
                b1, t1 = stack.pop()
                min_time += min(t1,t)
                if t1 > t:
                    stack.append((b1,t1))
                else:
                    stack.append((b,t))
            else:
                stack.append((b,t))
                res += min_time
                min_time = 0
        res += min_time
        return res
            
