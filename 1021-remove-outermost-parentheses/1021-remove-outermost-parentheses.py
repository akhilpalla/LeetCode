class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        stack=[]
        counter=0
        for i in S:
            if i=='(':
                counter=counter+1
                if counter==1:
                    pass
                else:
                    stack.append(i)
            else:
                counter=counter-1
                if counter == 0:
                    pass
                else:
                    stack.append(i)
        return (''.join(stack))