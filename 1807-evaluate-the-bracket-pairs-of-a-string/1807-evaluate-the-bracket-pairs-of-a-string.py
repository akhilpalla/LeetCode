class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know = dict(knowledge)

        res = []
        key = ""
        is_bracket = False

        for c in s:
            if c == "(":
                is_bracket = True
            elif c == ")":
                is_bracket = False
                res.append(know.get(key, "?"))
                key = ""
            elif is_bracket:
                key += c
            else:
                res.append(c)

        return "".join(res)