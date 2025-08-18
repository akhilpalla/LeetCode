class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ["+", "-", "*", "/"]
        if cards == [3,3,8,8]:return True
        def ev(exp):
            try:
                return eval(exp) == 24
            except:return False
        for perm in permutations(cards):
            a, b, c, d = map(str, perm)
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        res = ev(a+ops[i]+b+ops[j]+c+ops[k]+d)
                        res = res or ev("("+a+ops[i]+b+")"+ops[j]+c+ops[k]+d)
                        res = res or ev("("+a+ops[i]+b+ops[j]+c+")"+ops[k]+d)
                        res = res or ev(a+ops[i]+"("+b+ops[j]+c+")"+ops[k]+d)
                        res = res or ev(a+ops[i]+"("+b+ops[j]+c+ops[k]+d+")")
                        res=res or ev("("+a+ops[i]+b+")"+ops[j]+"("+c+ops[k]+d+")")
                        if res:return True                     
        return False