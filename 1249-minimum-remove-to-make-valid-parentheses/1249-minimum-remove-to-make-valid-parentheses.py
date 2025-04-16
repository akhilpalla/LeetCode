#CrackingFaang Solution
"""
Idea is to keep the count of left count and right count, greedly add all left counts
if we encounter a right check if we have enough left to match else skip

after parsing all the string check if left count and right count are equal, they might not be equal because we are greedly adding all left
so remove extra left from the right side
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lCount = rCount = 0

        filtered  = []

        for char in s:
            if char == "(":
                lCount += 1 
                filtered.append(char)
            
            elif char == ")":
                if lCount > rCount:
                    rCount += 1
                    filtered.append(char)
                
            else:
                filtered.append(char)
            
        if lCount == rCount:
            return "".join(filtered)
        
        else:
            res = []

            for i in range(len(filtered)-1 , -1 , -1):
                curChar = filtered[i]

                if curChar == '(':
                    if lCount == rCount:
                        res.append(curChar)
                    else:
                        lCount -=1
                    
                elif curChar == ")":
                    res.append(curChar)
                
                else:
                    res.append(curChar)

        return "".join(reversed(res))

# T = N
# S = N


"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_par = []
        s = list(s)
        
        for idc, char in enumerate(s):
            if char == '(':
                open_par.append(idc)
            elif char == ')':
                if open_par:
                    open_par.pop()
                else:
                    s[idc] = ""
                    
            
        while open_par:
            s[open_par.pop()] = ""
            
        return "".join(s)
"""