class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def to_postfix_notation():
            OPN = []
            stack = []
            p = ""
            for t in token():
                if "a" <= t[0] <= "z":
                    OPN.append(t)
                elif t in ",*":
                    while stack and stack[-1] == "*":
                        OPN.append(stack.pop())
                    stack.append(t)
                elif t == '{':
                    stack.append(t)
                elif t == '}':
                    while stack and stack[-1] != '{':
                        OPN.append(stack.pop())
                    stack.pop()
                p = t
            while stack:
                OPN.append(stack.pop())
            return OPN
        def token():
            i = 0
            while i < n:
                if expression[i] == "{":
                    if i == 0 or expression[i-1] in ",{":
                        yield expression[i]
                        i += 1
                    else:
                        yield "*"
                        yield expression[i]
                        i += 1
                elif expression[i] in "{},+":
                    yield expression[i]
                    i += 1
                elif "a" <= expression[i] <= "z":
                    if i > 0 and expression[i-1] == "}":
                        yield "*"
                        start = i
                        i += 1
                    else:
                        start = i
                    while i < n and "a" <= expression[i] <= "z":
                        i += 1
                    yield expression[start: i]
        n = len(expression)
        stack = []
        OPN = to_postfix_notation()
        for t in OPN:
            if "a" <= t[0] <= "z":
                stack.append(set([t]))
            elif t == ",":
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set1 | set2)
            elif t == "*":
                set2 = stack.pop()
                set1 = stack.pop()
                res = set()
                for s1 in set1:
                    for s2 in set2:
                        res.add(s1 + s2)
                stack.append(res)
        return sorted(stack[0])