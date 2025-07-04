class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        alpha = "zabcdefghijklmnopqrstuvwxy"
        track = 1
        logified = []
        ln = 2**len(operations)
        tempk = k
        ln /= 2
        while ln >= 1:
            if tempk > ln:
                logified.append(1)
                tempk -= ln
            else:
                logified.append(0)
            ln /= 2
        print(operations)
        logified.reverse()
        print(logified)
        for i in range(len(operations)):
            if operations[i] == 1 and logified[i] == 1:
                track += 1
        return alpha[mod(track, 26)]