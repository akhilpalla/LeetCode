class Solution:
    def minMaxDifference(self, num: int) -> int:
        l = list(str(num))
        max = 0
        min = 0
        max_change = -1
        min_change = l[0]
        for i in range(len(l)):
            if l[i] != '9':
                max_change = l[i]
                break
        for i in range(len(l)):
            max *= 10
            min *= 10
            max += 9 if l[i] == max_change else int(l[i])
            min += 0 if l[i] == min_change else int(l[i])
        return max - min