class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        context = []

        for c in s:
            match c:
                case '(':
                    stack.append(context)
                    context = []
                case ')':
                    context.reverse()
                    context = stack.pop() + context
                case _:
                    context.append(c)

        return ''.join(context)
        