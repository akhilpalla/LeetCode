class ExamRoom:

    def __init__(self, n: int):
        self.sl = SortedList()  
        self.n = n

    def seat(self) -> int:
        if not self.sl:
            self.sl.add(0)
            return 0
        
        diff, idx = self.sl[0], 0
       
        for x, y in pairwise(self.sl):
            if (y - x) // 2 > diff:
                diff = (y - x) // 2
                idx = x + (y - x) // 2

        if self.n - 1 - self.sl[-1] > diff:
            diff = self.n - 1 - self.sl[-1]
            idx = self.n - 1

        self.sl.add(idx)
        return idx

    def leave(self, p: int) -> None:
        self.sl.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)