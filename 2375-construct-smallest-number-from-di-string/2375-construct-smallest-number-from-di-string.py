class Solution:
    def smallestNumber(self, pattern: str) -> str:
        options = [str(x) for x in range(1, 10)]
        answer = ''
        new_set = options.pop(0)
        prev_p = None
        for i, p in enumerate(pattern):
            if p != prev_p:
                answer = answer + new_set[:-1]
                new_set = new_set[-1]
            if p == 'I':
                new_set = new_set + options.pop(0)
            if p == 'D':
                new_set = options.pop(0) + new_set
            prev_p = p
        answer = answer + new_set
        return answer